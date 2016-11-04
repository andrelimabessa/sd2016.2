import zmq
from common.common import Common
from common.serializer import Serializer


class Sock(object):
    def __init__(self):
        context = zmq.Context()
        self.sock = context.socket(zmq.DEALER)
        self.sock.setsockopt(zmq.IDENTITY, b'client')
        self.sock.connect("tcp://localhost:%s" % Common.CLIENT_ZMB_PORT)

    def send(self, data):
        self.sock.send_multipart([b'server', Serializer.to_binary_json(data)])

    def await(self):
        lista = self.sock.recv_multipart()
        dados = lista[len(lista) - 1:][0]
        return Serializer.from_binary_json(dados)

    def close(self):
        self.sock.close()
