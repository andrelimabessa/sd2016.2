import socket
from datetime import datetime




ENCODE = "UTF-8"
HOST = '127.0.0.1'   # Endereco IP do Servidor
PORT = 5000          # Porta que o Servidor esta
MAX_BYTES = 65535    # Quantidade de Bytes a serem ser recebidos


def client():
    text = input("Digite qualquer tecla para iniciar o jogo:\n")  # Recebe dados
    data = text.encode(ENCODE)  # Codifica para BASE64 os dados de entrada

    # Enviod de dados
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Inicializar um socket UDP
    dest = (HOST, PORT)  # Define IP de origem e Porta de destino
    sock.sendto(data, dest)  # Envia os dados para o destino
    while True:
        # Resposta de envio ao servidor
        #print(sock.getsockname())  # Imprime dados do socker de destino
        data, address = sock.recvfrom(MAX_BYTES)  # Recebendo dados
        text = data.decode(ENCODE)  # Convertendo dados de BASE64 para UTF-8

        if int(text) == 3:
            text = "Aguardando outro jogador"

        elif int(text) == 1:
            text = "Jogo iniciando"

        elif int(text) == 2:
            print("Faca sua jogada:")
            x = input("Informe a posicao do eixo X:")
            y = input("Informe a posicao do eixo Y:")
            text = x+","+y
            data = text.encode(ENCODE)
            sock.sendto(data, dest)  # Envia os dados para o destino

            # Resposta de envio ao servidor
            data, address = sock.recvfrom(MAX_BYTES)  # Recebendo dados
            text = data.decode(ENCODE)  # Convertendo dados de BASE64 para UTF-8

        elif int(text) == 4:
            text = "O outro jogador esta jogando"

        elif int(text) == 8:
            text = "Voce venceu!"

        elif int(text) == 7:
            text = "Voce Perdeu!"

        elif int(text) == 5:
            text = "Empate!"

        elif int(text) == 0:
            text = "Sem mais jogadas"




        print("\n\n"+text+"\n")  # Imprime texto e endereços
