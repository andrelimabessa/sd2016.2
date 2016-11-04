import logging

from common.common import Common
from server.processor import Processor
from server.socket import Sock


class Server(object):
    def __init__(self):
        self.logger = logging.getLogger("server")
        self.sock = Sock()

    def start(self):
        self.logger.info("Listening at %s" % Common.SERVER_PORT)
        while True:
            data = self.sock.await()
            self.logger.info("Got a connection")
            Processor(sock=self.sock, data=data).start()

    def shutdown(self):
        self.sock.close()
        self.logger.info("Server shutdown")
