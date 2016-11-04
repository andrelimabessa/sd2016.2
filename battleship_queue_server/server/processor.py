import logging
import threading

from common.protocol import Protocol
from server.storage import ServerStorage


class Processor(threading.Thread):

    def __init__(self, sock, data):
        super().__init__()
        self.sock = sock
        self.data = data
        self.storage = ServerStorage()
        self.logger = logging.getLogger(self.getName())
        self.logger.info('Criando thread')

    def send(self, data):
        self.sock.send(data)

    def send_status_response(self, status):
        self.send(data={'status': status})

    def send_data_response(self, status, data):
        self.send(data={'status': status, 'data': data})

    def run(self):
        value = self.data

        self.logger.info('Handling value: ' + str(value))
        request_type = value['type']
        _id = value['id']

        if _id is None:
            self.send_status_response(status=Protocol.Response.STATUS_FAILED)
        elif request_type == Protocol.Request.CONNECT:
            self.storage.create_files_if_needed(_id=_id)
            self.send_status_response(status=Protocol.Response.STATUS_SUCCESS)
        elif request_type == Protocol.Request.SAVE_BOARD:
            self.storage.save(_id=_id, data=value['data'])
            self.logger.info('Salvando dados: %s' % str(value['data']))
            self.send_status_response(status=Protocol.Response.STATUS_SUCCESS)
        elif request_type == Protocol.Request.LOAD_BOARD:
            if self.storage.has_data(_id=_id):
                state = self.storage.load_as_json(_id=_id)
                self.logger.info('Recuperando dados: %s' % str(state))
                self.send_data_response(status=Protocol.Response.STATUS_SUCCESS, data=state)
            else:
                self.send_status_response(status=Protocol.Response.STATUS_FAILED)
                self.logger.info('Finalizando processo')
