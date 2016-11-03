import socket
import BatalhaNaval
from datetime import datetime

ENCODE = "UTF-8"
MAX_BYTES = 65535
PORT = 5000            # Porta que o Servidor esta
HOST = ''     	       # Endereco IP do Servidor
a = ''

def enviar(address, text):
    orig = (HOST, PORT)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(orig)

    # Envia resposta
    data = text.encode(ENCODE)  # Codifica para BASE64 os dados
    sock.sendto(data, address)  # Enviando dados


def server():
    #Abrindo um socket UDP na porta 5000
    orig = (HOST, PORT)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(orig)

    while True:
        #recebi dados
        data, address = sock.recvfrom(MAX_BYTES) # Recebi dados do socket
        text = data.decode(ENCODE) # Convertendo dados de BASE64 para UTF-8
        #print(address, text)

        if int(text) == 1:
            a = BatalhaNaval.BatalhaNaval()
            # Envia resposta
            text = "1"
            data = text.encode(ENCODE) # Codifica para BASE64 os dados
            sock.sendto(data, address) # Enviando dados

        elif int(text) == 2:
            text = "2"
            if a.numMaximoJogadas == 0:
                text = "0"
                data = text.encode(ENCODE)  # Codifica para BASE64 os dados
                sock.sendto(data, address)
            else:
                data = text.encode(ENCODE)  # Codifica para BASE64 os dados
                sock.sendto(data, address)

                data, address = sock.recvfrom(MAX_BYTES)  # Recebi dados do socket
                text = data.decode(ENCODE)


                xy = text.split(",")
                text = a.jogada(int(xy[0]), int(xy[1]))
                data = text.encode(ENCODE)  # Codifica para BASE64 os dados
                sock.sendto(data, address)  # Enviando dados


        #Envia resposta
        #text = "Your data was " + str(len(data)) + " bytes long"
        #data = text.encode(ENCODE) # Codifica para BASE64 os dados
        #sock.sendto(data, address) # Enviando dados
