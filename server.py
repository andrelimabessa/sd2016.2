#coding: utf-8
import socket
from datetime import datetime
from BatalhaNaval import BatalhaNaval

ENCODE = "UTF-8"
MAX_BYTES = 65535
PORT = 5000            # Porta que o Servidor esta
HOST = '127.0.0.1'              # Endereco IP do Servidor

jogo = BatalhaNaval.carregar_jogo()

def server():
    #Abrindo um socket UDP na porta 5000
    orig = (HOST, PORT)                                                             
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(orig)

    while True:
        #recebi dados
        data, address = sock.recvfrom(MAX_BYTES) # Recebi dados do socket
        text = data.decode(ENCODE) # Convertendo dados de BASE64 para UTF-8

        print(text)
        dictData = eval(text)
        comando = dictData.get('comando')
        resposta = ""

        if comando == 0:
            resposta = "voce saiu"
        elif comando == 1:
            x = dictData.get('x')
            y = dictData.get('y')
            resposta = jogo.insere_navio(x, y)
        elif comando == 2:
            x = dictData.get('x')
            y = dictData.get('y')
            resposta = jogo.destroi_navio(x, y)
        elif comando == 3:
            resposta = jogo.exibe_tabuleiro_simples()
        elif comando == 4:
            jogo.salvar()
            resposta = "jogo salvo"

        # #Envia resposta
        data = resposta.encode(ENCODE) # Codifica para BASE64 os dados 
        sock.sendto(data, address) # Enviando dados 
        print(resposta)

    #Fechando Socket
    sock.close()

server()