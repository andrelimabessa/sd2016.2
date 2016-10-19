import batalhaNaval
import sys
import socket
from datetime import datetime

ENCODE = "UTF-8"
MAX_BYTES = 65535
PORT = 5000            # Porta que o Servidor esta
HOST = ''              # Endereco IP do Servidor

def server():
    #Abrindo um socket UDP na porta 5000
    orig = (HOST, PORT)                                                             
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(orig)

    jogador_um = 0
    jogador_dois = 0

    while True:
        #recebi dados
        data, address = sock.recvfrom(MAX_BYTES) # Recebi dados do socket
        text = data.decode(ENCODE) # Convertendo dados de BASE64 para UTF-8
        #print(address, text)

        if jogador_um == 0:
            jogador_um = address
            print("Jogador um entrou!")
        elif jogador_dois == 0:
            jogador_dois = address
            print("Jogador dois entrou!")

        #Envia resposta
        #text = "Your data was " + str(len(data)) + " bytes long"
        #data = text.encode(ENCODE) # Codifica para BASE64 os dados 
        #sock.sendto(data, address) # Enviando dados 

    #Fechando Socket
    sock.close()

server()
