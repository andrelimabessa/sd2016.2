import logging
import socket
import sys

from common.common import Common
from server.processor import Processor


class Server(object):
    def __init__(self):
        self.logger = logging.getLogger("server")
        self.threads = []

    def __bind(self, origin):

        sock = socket.socket(
            socket.AF_INET,  # Internet
            socket.SOCK_DGRAM  # UDP
        )
        try:
            sock.bind(origin)
            return sock
        except socket.error as msg:
            print("Socket Error: %s" % msg)
        except TypeError as msg:
            print("Type Error: %s" % msg)


    def __wait__(self, sock):
        return sock.recvfrom(Common.BYTES)

    def start(self):

        try:
            origin = ("0.0.0.0", Common.PORT)
            self.logger.info("Listening at %s:%s" % (origin[0], str(origin[1])))
            sock = self.__bind(origin=origin)

            while True:
                data, address = self.__wait__(sock=sock)
                self.logger.info("Got a connection")
                thread = Processor(sock=sock, address=address, data=data)
                self.threads.append(thread)
                thread.start()
        except:
            pass


    def shutdown(self):
        for thread in self.threads:
            if thread.isAlive():
                self.logger.warn('Killing thread %s' % thread.getName())
                thread._Thread__stop()
        self.logger.info("Server shutdown")
