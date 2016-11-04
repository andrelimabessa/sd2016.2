from jsonrpclib import Server

from client.board import Board
from client.console import Console
from client.exception.invalid_column_value import InvalidColumnValueException
from client.exception.invalid_row_value import InvalidRowValueException
from client.exception.max_move_exceeded import MaxMoveValueExceededException
from client.printer import Printer
from client.storage import ClientStorage
from common.common import Common
from common.protocol import Protocol
from common.unit import Unit


class Client(object):
    MOVE = '1'
    BOARD = '2'
    REAL_BOARD = '3'
    RESTART = '4'
    CLEAR = '5'
    EXIT = '6'

    def __init__(self):
        self.board = Board()
        self.proxy = Server('http://%s:%s' % (Common.HOST, str(Common.PORT)))

    def __print_board_legend(self):
        print(' ~ = Agua')
        print(' 🚤 = Navio')
        print(' ! = Abatido')
        print(' 💣 = Bomba', end='\n\n')

    def start(self):
        self.connect()
        self.load_board()

        Printer.print_choice()
        choice = input('Escolha uma opção:\n')

        while choice != Client.EXIT:
            Console.clear()
            Printer.print_remaining_moves(self.board.remaining_moves())

            if choice == Client.MOVE:
                self.print_board()
                self.move()
            elif choice == Client.BOARD:
                self.print_board()
            elif choice == Client.REAL_BOARD:
                self.print_real_board()
            elif choice == Client.RESTART:
                self.restart_board()
            elif choice == Client.CLEAR:
                Console.clear()
            else:
                Printer.print_invalid_choice()

            Printer.print_choice()
            choice = input('Escolha uma opção:\n')

    def connect(self):
        username = input('Informe seu apelido ...\n')
        status = self.proxy.connect(username)

        if status == Protocol.Response.STATUS_SUCCESS:
            self.id = username
            self.storage = ClientStorage(_id=username)
        else:
            Printer.print_connecting_error()
            self.connect()

    def move(self):
        row = input('>> Linha.\n')
        col = input('>> Coluna.\n')

        try:
            self.board.move(row=int(row), col=int(col))
            self.save_board()
        except (
                InvalidRowException, InvalidColumnException,
                MaxMoveExceededException) as e:
            Printer.print_exception(exception=e)
            Printer.print_message('Ignoring this move per now.\n')

    def restart_board(self):
        self.board.restart()
        self.save_board()

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

    def print_real_board(self):
        self.__print_board_legend()
        print('------------- Tabuleiro -------------', end='\n\n')
        for x in range(self.board.rows):
            for y in range(self.board.cols):
                value = self.board.board[x][y]
                if value == Unit.WATER:
                    print(' ~ ', end=' ')
                elif value == Unit.SHIP:
                    print(' 🚤 ', end=' ')
                elif value == Unit.SUNK_SHIP:
                    print(' ! ', end=' ')
                else:
                    print(' 💣 ', end=' ')
            print('')
        print('')

    def load_board(self):
        if self.storage.has_data():
            self.board.load_from_state(state=self.storage.load_state())
            self.save_board()
        else:
            result = self.proxy.load_board(self.id)
            status = result['status']

            if status == Protocol.Response.STATUS_SUCCESS:
                self.board.load_from_state(state=result['data'])

            self.save_board()

    def save_board(self):
        board_state = self.board.state()

        status = self.proxy.save_board(self.id, board_state)
        self.storage.save_state(state=board_state)

        if status == Protocol.Response.STATUS_FAILED:
            Printer.print_message('ERRO ao tenter enviar tabeleiro ao servidor!')
