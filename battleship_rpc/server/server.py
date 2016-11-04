import logging

from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer

from common.common import Common
from server.processor import Processor


class Server(object):
    def __init__(self):
        self.logger = logging.getLogger('server')
        self.processor = Processor()

    def start(self):
        self.logger.info('Listening at %s' % str(Common.PORT))
        server = SimpleJSONRPCServer((Common.HOST, Common.PORT))

        server.register_function(self.processor.connect)
        server.register_function(self.processor.save_board)
        server.register_function(self.processor.load_board)
        server.serve_forever()
