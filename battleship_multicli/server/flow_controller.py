import socket

from common.board import Board
from common.protocol import Protocol
from server.clients_controller import ClientsController
from server.socket import Sock


class FlowController(object):
    @staticmethod
    def start_game(_id, active, storage):
        pair = ClientsController.get_pair(_id=_id, active=active)
        first_id = pair[0][0]
        second_id = pair[1][0]
        storage_key = '%s_%s' % (str(first_id), str(second_id))
        board = Board()

        storage.save(key=storage_key, data={
            first_id: board.new_state(),
            second_id: board.new_state()
        })

    @staticmethod
    def bind(origin):
        sock = socket.socket(
            socket.AF_INET,  # Internet
            socket.SOCK_DGRAM  # UDP
        )

        sock.bind(origin)

        return sock

    @staticmethod
    def disconnect_pair(requester_id, active, sock):
        if ClientsController.is_active(_id=requester_id, active=active):
            pair = ClientsController.get_pair(_id=requester_id, active=active)
            ClientsController.remove_pair(_id=requester_id, active=active)
            Sock.send(sock=sock,
                      address=ClientsController.get_address(pair=pair, _id=requester_id),
                      data={'status': Protocol.Response.STATUS_SUCCESS})
            Sock.send(sock=sock,
                      address=ClientsController.get_other_address(pair=pair, _id=requester_id),
                      data={'status': Protocol.Response.STATUS_SUCCESS, 'connected': False})
