import socket
from datetime import datetime




ENCODE = "UTF-8"
HOST = ''   # Endereco IP do Servidor
PORT = 50007          # Porta que o Servidor esta
MAX_BYTES = 65535    # Quantidade de Bytes a serem ser recebidos


def client():
    """ Procedimento responsável por enviar dados para o servidor e receber alguma resposta por conta disso """
    while True:
        print ("1 - Novo Jogo")
        print("2 - Fazer jogada")
        text = input("Digite uma opcao:\n")  # Recebe dados
        data = text.encode(ENCODE)  # Codifica para BASE64 os dados de entrada

        # Enviod de dados
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Inicializar um socket UDP
        dest = (HOST, PORT)  # Define IP de origem e Porta de destino
        sock.sendto(data, dest)  # Envia os dados para o destino

        # Resposta de envio ao servidor
        #print(sock.getsockname())  # Imprime dados do socker de destino
        data, address = sock.recvfrom(MAX_BYTES)  # Recebendo dados
        text = data.decode(ENCODE)  # Convertendo dados de BASE64 para UTF-8

        if int(text) == 0:
            text = "Suas jogadas acabaram, inicie um novo jogo!"

        elif int(text) == 1:
            text = "Novo Jogo Iniciado"

        elif int(text) == 2:
            x = input("Digite a posicao do eixo X:")
            y = input("Digite a posicao do eixo Y:")
            text = x+","+y
            data = text.encode(ENCODE)
            sock.sendto(data, dest)  # Envia os dados para o destino

            # Resposta de envio ao servidor
            data, address = sock.recvfrom(MAX_BYTES)  # Recebendo dados
            text = data.decode(ENCODE)  # Convertendo dados de BASE64 para UTF-8



        print("\n\n"+text+"\n")  # Imprime texto e endereços
