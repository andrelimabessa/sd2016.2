import logging

from client.client import Client
from server.server import Server
from queue_server.queue_server import QueueServer


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

        @staticmethod
        def queue_server():
            Inicializador.start()
            try:
                queue_server = QueueServer()
                queue_server.start()
                logging.info("Servidor de fila pronto")
            except (KeyboardInterrupt, SystemExit):
                pass
            except:
                logging.exception("Erro no servidor de fila!")
                raise
            finally:
                queue_server.shutdown()
