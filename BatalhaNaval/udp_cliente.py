import socket
from datetime import datetime
from menu import Menu

ENCODE = "UTF-8"
HOST = '127.0.0.1'  # Endereco IP do Servidor
PORT = 5000          # Porta que o Servidor esta
MAX_BYTES = 65535

def client():

    exibe = Menu()
    """ Procedimento responsável por enviar dados para o servidor e receber alguma resposta por conta disso """

    while True:
        #Envio de dados
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        dest = (HOST, PORT)
        text = exibe.exibeMenu()
        data = text.encode(ENCODE)
        sock.sendto(data, dest)

        #Resposta de envio ao servidor
        data, address = sock.recvfrom(MAX_BYTES)  # Danger! See Chapter 2
        text = data.decode(ENCODE)
        print(text)

    #print(address, text)
