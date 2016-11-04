import logging

from common.protocol import Protocol
from server.file import ServerFile


class Processor(object):
    def __init__(self):
        self.file = ServerFile()
        self.logger = logging.getLogger('Thread')

    def connect(self, _id):
        self.file.create_files_if_needed(_id=_id)
        return Protocol.Response.STATUS_SUCCESS

    def save_board(self, _id, data):
        self.file.save(_id=_id, data=data)
        self.logger.info('Salvando dados: %s' % str(data))
        return Protocol.Response.STATUS_SUCCESS

    def load_board(self, _id):
        if self.file.has_data(_id=_id):
            state = self.file.load_as_json(_id=_id)
            self.logger.info('Recuperando dados: %s' % str(state))
            return {'status': Protocol.Response.STATUS_SUCCESS, 'data': state}
        else:
            return {'status': Protocol.Response.STATUS_FAILED}
