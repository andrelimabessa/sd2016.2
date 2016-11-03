import socket
import BatalhaNavalSD
from datetime import datetime

ENCODE = "UTF-8"
HOST = '127.0.0.1'   # Endereco IP do Servidor
PORT = 5000          # Porta que o Servidor esta
MAX_BYTES = 65535    # Quantidade de Bytes a serem ser recebidos

def client():
    """ Procedimento responsável por enviar dados para o servidor e receber alguma resposta por conta disso """
    partida = BatalhaNavalSD.batalhaNaval(3)
    while partida.numJogadas > 0:
        partida.jogada()
        # Envio de dados
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Inicializar um socket UDP
        dest = (HOST, PORT)  # Define IP de origem e Porta de destino
        sock.sendto(data, dest)  # Envia os dados para o destino

        if partida.numBarcos == 0:
            text = print("Você destruiu todos os barco,Parabéns!")
            data = text.encode(ENCODE)
            break
        elif partida.numBarcos > 0 and partida.numJogadas > 0:
            text = print("Você ainda possui " + str(partida.numJogadas) + " jogada(s).")
            data = text.encode(ENCODE)
        else:
            text = print("Acabaram suas jogadas!")
            data = text.encode(ENCODE)
    print("Fim de Jogo")
    text = input("Digite algum texto:\n")   		    # Recebe dados
    data = text.encode(ENCODE)				    # Codifica para BASE64 os dados de entrada
    

    #Resposta de envio ao servidor
    print(sock.getsockname())				    # Imprime dados do socker de destino
    data, address = sock.recvfrom(MAX_BYTES)                # Recebendo dados
    text = data.decode(ENCODE)                              # Convertendo dados de BASE64 para UTF-8
    print(address, text)                                    # Imprime texto e endereços

    partida.limparLogs()