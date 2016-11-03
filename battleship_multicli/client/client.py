from client.console import Console
from client.socket import Sock
from common.board import Board
from common.protocol import Protocol
from common.unit import Unit

class Client(object):
    def __init__(self):
        self.sock = Sock()
        self.board = Board()
        self.id = None

    def __print_board_legend(self):
        print(' ~ = Agua')
        print(' 🚤 = Navio')
        print(' ! = Abatido')
        print(' 💣 = Bomba', end='\n\n')

    def start(self):
        response = self.connect()
        self.load_board()
        self.__handle_await_response(response=response)

    def __handle_await_response(self, response):
        if response['status'] == Protocol.Response.STATUS_FAILED:

            print('Tente novamente...')
            response['status'] = Protocol.Response.STATUS_SUCCESS
            self.__handle_await_response(response=response)

        elif 'connected' in response:
            print('\nYou lose. :( sorry\n')

        elif 'result' in response['data']:
            print('\nVocê ganhou :)\n' if response['data']['result'] else '\nYou lose :(\n')
            print('Inté! :)')
            self.shutdown()

        elif response['data']['you_play']:

            Console.clear()
            self.print_board()
            print('>>Você Joga ... :)')

            move_success = self.move()

            if move_success:
                Console.clear()
                self.print_board()
                print('>>Adversário joga ...')
                self.__handle_await_response(response=self.await())
            else:
                self.__handle_await_response(response=response)
        else:
            print('>>Adversário joga ...')
            self.__handle_await_response(response=self.await())

    def shutdown(self):
        self.disconnect()
        self.sock.close()

    def connect(self):
        username = input('Informe seu apelido...\n')
        self.send_connection_request(username=username)

        result = self.await()
        status = result['status']

        if status == Protocol.Response.STATUS_AWAITING:
            print('\n>>Aguardando adversário!')
            result = self.await()
            status = result['status']

        if status == Protocol.Response.STATUS_SUCCESS:
            self.id = username
            print('\n>>Jogando com \"%s\". :)\n' % str(result['data']['opponent']))
            return result
        else:
            print('ERRO ao tentar conectar com servidor server!!!')
            return self.connect()

    def disconnect(self):
        if self.id is not None:
            self.send_disconnection_request(username=self.id)

    def move(self):
        row = input('>> Linha.\n')
        col = input('>> Coluna.\n')

        #if self.is_value_integer(row) and self.is_value_integer(col):
        if row.isdigit() and col.isdigit():

            self.send_move_request(username=self.id, row=int(row), col=int(col))

            result = self.await()
            status = result['status']

            if status == Protocol.Response.STATUS_SUCCESS:
                self.board.move(row=int(row), col=int(col))
                return True
            else:
                print('\nLinha ou Coluna inválida ...\n\n')
                return False

    def print_board(self):
        self.__print_board_legend()

        print('------------- Tabuleiro -------------', end='\n\n')

        for x in range(self.board.rows):
            for y in range(self.board.cols):
                value = self.board.board[x][y]
                if value == Unit.WATER or value == Unit.SHIP:
                    print(' ~ ', end=' ')
                elif value == Unit.SUNK_SHIP:
                    print(' ! ', end=' ')
                else:
                    print(' 💣 ', end=' ')
            print('')
        print('')

    def load_board(self):
        self.send_load_board_request(username=self.id)

        result = self.await()
        status = result['status']

        if status == Protocol.Response.STATUS_SUCCESS:
            self.board.load_from_state(state=result['data'])

    def save_board(self):
        board_state = self.board.state()
        self.send_save_board_request(username=self.id, state=board_state)

        result = self.await()
        status = result['status']

        if status == Protocol.Response.STATUS_FAILED:
            print('ERRO ao tenter enviar tabeleiro ao servidor!')

    def await(self):
        return self.sock.await()

    def send_connection_request(self, username):
        self.sock.send(data={'type': Protocol.Request.CONNECT, 'id': username})

    def send_disconnection_request(self, username):
        self.sock.send(data={'type': Protocol.Request.DISCONNECT, 'id': username})

    def send_load_board_request(self, username):
        self.sock.send(data={'type': Protocol.Request.LOAD_BOARD, 'id': username})

    def send_save_board_request(self, username, state):
        self.sock.send(data={'type': Protocol.Request.SAVE_BOARD, 'id': username, 'data': state})

    def send_move_request(self, username, row, col):
        self.sock.send(data={
            'type': Protocol.Request.MOVE,
            'id': username,
            'data': {'row': row, 'col': col}
        })

    def is_value_integer(self, number):
        try:
            int(number)
        except ValueError:
            return False
        else:
            return True
        return True
