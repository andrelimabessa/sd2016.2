import logging

from client.client import Client
from server.server import Server


class Inicializador(object):
    @staticmethod
    def start():
        logging.basicConfig(level=logging.DEBUG)

    @staticmethod
    def client():

        Inicializador.start()
        try:
            client = Client()
            client.start()
            logging.info("Cliente pronto")
        except (KeyboardInterrupt, SystemExit):
            pass
        except:
            logging.exception("Erro no cliente!")


    @staticmethod
    def server():

        Inicializador.start()
        try:
            server = Server()
            server.start()
            logging.info("Servidor pronto")
        except (KeyboardInterrupt, SystemExit):
            pass
        except:
            logging.exception("Erro no servidor!")
            raise
        finally:
            server.shutdown()
