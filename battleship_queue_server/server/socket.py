import zmq

from common.serializer import Serializer
from common.common import Common


class Sock(object):
    def __init__(self):
        context = zmq.Context()
        self.sock = context.socket(zmq.DEALER)
        self.sock.setsockopt(zmq.IDENTITY, b'server')
        self.sock.connect("tcp://localhost:%s" % Common.SERVER_ZMB_PORT)

    def send(self, data):
        print('Recuperando dados: %s' % str(data))
        self.sock.send_multipart([b'client', Serializer.to_binary_json(data)])

    def await(self):
        lista = self.sock.recv_multipart()
        print('List >>: %s' % str(lista))
        dados = lista[len(lista) - 1:][0]
        print('Dados >>: %s' % str(dados))
        return Serializer.from_binary_json(dados)

    def close(self):
        self.sock.close()
