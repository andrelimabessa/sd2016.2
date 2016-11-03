import socket
from datetime import datetime
from jogo import *
import ast
ENCODE = "UTF-8"
MAX_BYTES = 65535
PORT = 5000            # Porta que o Servidor esta
HOST = ''     # Endereco IP do Servidor

def server():
    #Abrindo uma porta UDP
    orig = (HOST, PORT)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(orig)
    while True:
        #recebi dados
        data, address = sock.recvfrom(MAX_BYTES)
        text = data.decode(ENCODE)
        map = ast.literal_eval(text)
        text = map["opcao"]
        if text == "1":
            jogo = BatalhaNaval()
            jogo.insereNavios()
            resp = "Tabuleiro criado"
        elif text == "2":
            resp = jogo.jogada(map["posX"], map["posY"])
        else:
            resp = "Opção Inválida!"
       
        data = resp.encode(ENCODE)
        sock.sendto(data, address)
    sock.close()
