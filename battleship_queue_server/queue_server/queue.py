import logging
import zmq
from common.common import Common

class QueueServer(object):
    @staticmethod
    def start():
        try:
            logging.info('Iniciando servidor de fila ....')
            context = zmq.Context(1)

            client_socket = context.socket(zmq.XREP)
            client_socket.bind("tcp://*:%s" % Common.CLIENT_PORT)

            server_socket = context.socket(zmq.XREQ)
            server_socket.bind("tcp://*:%s" % Common.SERVER_PORT)

            zmq.device(zmq.QUEUE, client_socket, server_socket)
        except:
            logging.exception("ERRO: no servidor de Fila!")
        finally:
            client_socket.close()
            server_socket.close()
context.term()
