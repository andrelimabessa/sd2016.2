import logging
import threading

from common.protocol import Protocol
from common.serializer import Serializer
from server.file import ServerFile


class Processor(threading.Thread):
    def __init__(self, sock, address, data):
        super().__init__()
        self.sock = sock
        self.address = address
        self.data = data
        self.file = ServerFile()
        self.logger = logging.getLogger(self.getName())
        self.logger.info('Criando processo ...')

    def __deserialize_data(self):
        return Serializer.from_binary_json(data=self.data)

    def __send(self, data):
        self.sock.sendto(Serializer.to_binary_json(data), self.address)

    def __send_status_response(self, status):
        self.__send(data={'status': status})

    def __send_data_response(self, status, data):
        self.__send(data={'status': status, 'data': data})

    def run(self):
        value = self.__deserialize_data()

        self.logger.info('Handling value: ' + str(value))
        request_type = value['type']
        _id = value['id']

        if _id is None:
            self.__send_status_response(status=Protocol.Response.STATUS_FAILED)

        elif request_type == Protocol.Request.CONNECT:
            self.file.create_files_if_needed(_id=_id)
            self.__send_status_response(status=Protocol.Response.STATUS_SUCCESS)

        elif request_type == Protocol.Request.SAVE_BOARD:
            self.file.save(_id=_id, data=value['data'])
            self.logger.info('Salvando dados: %s' % str(value['data']))
            self.__send_status_response(status=Protocol.Response.STATUS_SUCCESS)

        elif request_type == Protocol.Request.LOAD_BOARD:

            if self.file.has_data(_id=_id):
                state = self.file.load_as_json(_id=_id)
                self.logger.info('Recuperando dados: %s' % str(state))
                self.__send_data_response(status=Protocol.Response.STATUS_SUCCESS, data=state)
            else:
                self.__send_status_response(status=Protocol.Response.STATUS_FAILED)

        self.logger.info('Finalizando processo')
