import socket
import BattleShip
from datetime import datetime

ENCODE = "UTF-8"
HOST = ''   # O nome do meu host pode ser : localhost ; 0.0.0.0 ; 127.0.0.1
PORT = 50007           # Vai utilizar está porta
MAX_BYTES = 65535    # Quantidade de Bytes a serem ser recebidos

def client():
    """ Procedimento responsável por enviar dados para o servidor e receber alguma resposta por conta disso """
    partida = BattleShip.batalhaNaval(3)
    while partida.qtdJogadas > 0:
        partida.jogada()
        # Envio de dados
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Inicializar um socket UDP
        dest = (HOST, PORT)  # Define IP de origem e Porta de destino
        sock.sendto(data, dest)  # Envia os dados para o destino

        if partida.qtdBarcos == 0:
            text = print("Destruído todos os Barcos. Congratulations!!")
            data = text.encode(ENCODE)
            break
        elif partida.qtdBarcos > 0 and partida.qtdJogadas > 0:
            text = print("Ainda restam " + str(partida.qtdJogadas) + " jogada(s).")
            data = text.encode(ENCODE)
        else:
            text = print("Fim das suas jogadas!")
            data = text.encode(ENCODE)
    print("Game Over")
    text = input("Digite Aqui:\n")   		         # Recebe dados
    data = text.encode(ENCODE)				    # Codifica para BASE64 os dados de entrada
    

    #Resposta de envio ao servidor
    print(sock.getsockname())				    # Imprime dados do socker de destino
    data, address = sock.recvfrom(MAX_BYTES)                # Recebendo dados
    text = data.decode(ENCODE)                              # Convertendo dados de BASE64 para UTF-8
    print(address, text)                                    # Imprime texto e endereços

    partida.limparLogs()
