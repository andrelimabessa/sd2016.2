import socket

from common.common import Common
from common.serializer import Serializer


class Sock(object):
    def __init__(self):
        self.sock = socket.socket(
            socket.AF_INET,  # Internet
            socket.SOCK_DGRAM  # UDP
        )
        self.destination = (Common.HOST, Common.PORT)

    def send(self, data):
        self.sock.sendto(Serializer.to_binary_json(data), self.destination)

    def await(self):
        data, address = self.sock.recvfrom(Common.BYTES)  # Buffer size is Common.BYTES bytes
        return Serializer.from_binary_json(data)

    def close(self):
        self.sock.close()
