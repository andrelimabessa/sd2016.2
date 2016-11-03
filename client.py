#coding: utf-8
import socket
from datetime import datetime

ENCODE = "UTF-8"
HOST = 'localhost'   # Endereco IP do Servidor
PORT = 5000          # Porta que o Servidor esta
MAX_BYTES = 65535    # Quantidade de Bytes a serem ser recebidos

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Inicializar um socket UDP
dest = (HOST, PORT)                                     # Define IP de origem e Porta de destino 

def mostra_menu():
    print("---------- BATALHA NAVAL ----------")
    print("'0' para sair\n")
    print("'1' para inserir navio\n")
    print("'2' para destruir navio\n")
    print("'3' para exibir o tabuleiro\n")
    print("'4' para salvar o jogo\n")

def executa_comando(comando):
    if comando == 0:
        return 0
    elif comando == 1:
        x = int(input('Insira a posição X para inserir navio: '))
        y = int(input('Insira a posição y para inserir navio: '))
        print(x, y)
        data = str({"comando": 1, "x": x, "y": y}).encode(ENCODE)
        sock.sendto(data, dest)

        data, address = sock.recvfrom(MAX_BYTES)                # Recebendo dados
        text = data.decode(ENCODE)                              # Convertendo dados de BASE64 para UTF-8
        print(text)
    elif comando == 2:
        x = int(input('Insira a posição X para destruir navio: '))
        y = int(input('Insira a posição y para destruir navio: '))
        print(x, y)
        data = str({"comando": 2, "x": x, "y": y}).encode(ENCODE)
        sock.sendto(data, dest)

        data, address = sock.recvfrom(MAX_BYTES)                # Recebendo dados
        text = data.decode(ENCODE)                              # Convertendo dados de BASE64 para UTF-8
        print(text)
    elif comando == 3:
        data = str({"comando": 3}).encode(ENCODE)
        sock.sendto(data, dest)

        data, address = sock.recvfrom(MAX_BYTES)                # Recebendo dados
        text = data.decode(ENCODE) 
        print(text)
    elif comando == 4:
        data = str({"comando": 4}).encode(ENCODE)
        sock.sendto(data, dest)

        data, address = sock.recvfrom(MAX_BYTES)                # Recebendo dados
        text = data.decode(ENCODE) 
        print(text)

def client():
    """ Procedimento responsável por enviar dados para o servidor e receber alguma resposta por conta disso """

    text = input("Digite algum texto:\n")   		    # Recebe dados
    data = text.encode(ENCODE)				    # Codifica para BASE64 os dados de entrada	
    
    #Enviod de dados                                # Define IP de origem e Porta de destino  
    sock.sendto(data, dest)                                 # Envia os dados para o destino

    #Resposta de envio ao servidor
    # print(sock.getsockname())				    # Imprime dados do socker de destino
    data, address = sock.recvfrom(MAX_BYTES)                # Recebendo dados
    text = data.decode(ENCODE)                              # Convertendo dados de BASE64 para UTF-8
    print(address, text)                                    # Imprime texto e endereços

def inicia_jogo():
    jogando = 1
    while jogando != 0:
        mostra_menu()       
        comando = input('Insira um comando: ')
        jogando = executa_comando(int(comando))

    print("FIM DO JOGO")
        
inicia_jogo()