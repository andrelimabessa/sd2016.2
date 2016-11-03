import logging

from common.common import Common
from common.protocol import Protocol
from common.serializer import Serializer
from server.clients_controller import ClientsController
from server.flow_controller import FlowController
from server.processor import Processor
from server.socket import Sock
from server.file import ServerFile


class Server(object):
    def __init__(self):
        self.logger = logging.getLogger("server")
        self.storage = ServerFile()
        self.threads = []
        self.awaiting = None
        self.active = []

    def __wait__(self, sock):
        return sock.recvfrom(Common.BYTES)

    def start(self):
        origin = ("0.0.0.0", Common.PORT)
        self.logger.info("Listening at %s:%s" % (origin[0], str(origin[1])))

        sock = FlowController.bind(origin=origin)

        while True:
            data, address = self.__wait__(sock=sock)
            value = Serializer.from_binary_json(data=data)
            _id = value['id']
            _type = value['type']

            self.logger.info('Handling value: ' + str(value))

            if _id is None:
                Sock.send_status(sock=sock, address=address, status=Protocol.Response.STATUS_FAILED)
            elif _type == Protocol.Request.DISCONNECT:
                self.logger.warn('Disconnecting pair: [%s]' % str(self.active))
                FlowController.disconnect_pair(sock=sock, requester_id=_id, active=self.active)
            elif self.awaiting is None and not ClientsController.is_active(_id=_id,
                                                                           active=self.active):
                self.awaiting = (_id, address)
                Sock.send_status(sock=sock, address=address,
                                 status=Protocol.Response.STATUS_AWAITING)
            elif ClientsController.is_active(_id=_id, active=self.active):
                thread = Processor(sock=sock, requester_id=_id,
                                   pair=ClientsController.get_pair(_id=_id, active=self.active),
                                   data=value)
                self.threads.append(thread)
                thread.setDaemon(True)
                thread.start()
            else:
                first = self.awaiting
                second = (_id, address)
                self.logger.info('Binding "%s" and "%s"' % (str(first[0]), str(second[0])))

                self.active.append((first, second))
                self.awaiting = None

                FlowController.start_game(_id=_id, active=self.active, storage=self.storage)

                Sock.send(sock=sock, address=first[1],
                          data={
                              'status': Protocol.Response.STATUS_SUCCESS,
                              'data': {
                                  'opponent': second[0],
                                  'you_play': True
                              }
                          })
                Sock.send(sock=sock, address=second[1],
                          data={
                              'status': Protocol.Response.STATUS_SUCCESS,
                              'data': {
                                  'opponent': first[0],
                                  'you_play': False
                              }
                          })

            self.logger.info('Active clients: %s' % str(self.active))
            self.logger.info('Awaiting client: %s' % str(self.awaiting))

    def shutdown(self):
        for thread in self.threads:
            if thread.isAlive():
                self.logger.warn('Killing thread %s' % thread.getName())
                thread._Thread__stop()
        self.logger.info("Server shutdown")
