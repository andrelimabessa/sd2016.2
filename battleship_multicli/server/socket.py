from common.serializer import Serializer

class Sock(object):
    @staticmethod
    def send(sock, address, data):
        sock.sendto(Serializer.to_binary_json(data), address)

    @staticmethod
    def send_status(sock, address, status):
        Sock.send(sock=sock, address=address, data={'status': status})
