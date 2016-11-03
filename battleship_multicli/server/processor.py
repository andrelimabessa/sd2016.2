import logging
import threading

from common.board import Board
from common.exception.invalid_column import InvalidColumnException
from common.exception.invalid_row import InvalidRowException
from common.exception.max_move_exceeded import MaxMoveExceededException
from common.protocol import Protocol
from server.clients_controller import ClientsController
from server.socket import Sock
from server.file import ServerFile


class Processor(threading.Thread):
    def __init__(self, sock, requester_id, pair, data):
        super().__init__()
        self.sock = sock
        self.requester_id = requester_id
        self.pair = pair
        self.data = data
        self.board = Board()
        self.file = ServerFile()
        self.logger = logging.getLogger(self.getName())
        self.logger.info('Creating process')

    def send_status(self, address, status):
        Sock.send(sock=self.sock, address=address, data={'status': status})

    def send_data(self, address, status, data):
        Sock.send(sock=self.sock, address=address, data={'status': status, 'data': data})

    def save_board(self, storage_key, value):
        content = self.file.load_as_json(key=storage_key)
        content[self.requester_id] = value['data']
        self.file.save(key=storage_key, data=content)
        self.logger.info('Saving data: %s' % str(value['data']))
        self.send_status(address=ClientsController.get_address(pair=self.pair,
                                                                          _id=self.requester_id),
                                    status=Protocol.Response.STATUS_SUCCESS)

    def load_board(self, storage_key):
        if self.file.has_data(key=storage_key):
            content = self.file.load_as_json(key=storage_key)
            state = content[self.requester_id]
            self.logger.info('Returning data: %s' % str(state))
            self.send_data(
                address=ClientsController.get_address(pair=self.pair, _id=self.requester_id),
                status=Protocol.Response.STATUS_SUCCESS,
                data=state)
        else:
            self.send_status(
                address=ClientsController.get_address(pair=self.pair, _id=self.requester_id),
                status=Protocol.Response.STATUS_FAILED)

    def disconnect(self):
        self.logger.info('Disconnecting user %s' % str(self.requester_id))

    def handle_invalid_type(self):
        self.send_status(
            address=ClientsController.get_address(pair=self.pair, _id=self.requester_id),
            status=Protocol.Response.STATUS_FAILED)

    def move(self, storage_key, value):
        if self.file.has_data(key=storage_key):
            content = self.file.load_as_json(key=storage_key)
            state = content[self.requester_id]
            self.board.load_from_state(state=state)
            data = value['data']

            try:
                self.board.move(row=data['row'], col=data['col'])
                content[self.requester_id] = self.board.state()
                self.file.save(key=storage_key, data=content)
                return True
            except (InvalidRowValueException, InvalidColumnValueException,
                    MaxMoveValueExceededException) as e:
                self.logger.exception(e)
                return False
        else:
            return False

    def run(self):
        value = self.data

        request_type = value['type']
        storage_key = ClientsController.resolve_storage_key(_id=self.requester_id,
                                                            pair=self.pair,
                                                            storage=self.file)

        requester_address = ClientsController.get_address(pair=self.pair, _id=self.requester_id)
        other_id = ClientsController.get_other_id(pair=self.pair, _id=self.requester_id)
        other_address = ClientsController.get_other_address(pair=self.pair, _id=self.requester_id)

        if request_type == Protocol.Request.MOVE:
            move_success = self.move(storage_key=storage_key, value=value)

            if move_success:
                content = self.file.load_as_json(key=storage_key)

                self.board.load_from_state(state=content[self.requester_id])
                other_won = self.board.won()

                self.board.load_from_state(state=content[other_id])
                requester_won = self.board.won()

                if requester_won or other_won:
                    self.send_data(address=requester_address,
                                status=Protocol.Response.STATUS_SUCCESS,
                                data={
                                  'you_play': False,
                                  'result': requester_won
                              })
                    self.send_data(address=other_address,
                              status=Protocol.Response.STATUS_SUCCESS,
                              data={
                                  'you_play': True,
                                  'result': other_won
                              })
                else:
                    self.send_data(address=requester_address,
                              status=Protocol.Response.STATUS_SUCCESS,
                              data={'you_play': False})
                    self.send_data(address=other_address,
                              status=Protocol.Response.STATUS_SUCCESS,
                              data={'you_play': True})
            else:
                self.send_data(address=requester_address,
                              status=Protocol.Response.STATUS_FAILED,
                              data={'you_play': True})

        elif request_type == Protocol.Request.SAVE_BOARD:
            self.save_board(storage_key=storage_key, value=value)
        elif request_type == Protocol.Request.LOAD_BOARD:
            self.load_board(storage_key=storage_key)
        elif request_type == Protocol.Request.DISCONNECT:
            self.disconnect()
        else:
            self.handle_invalid_type()

        self.logger.info('Finishing process')
