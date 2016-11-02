import socket
import BatalhaNaval
from datetime import datetime
import threading

ENCODE = "UTF-8"
MAX_BYTES = 65535
PORT = 5000            # Porta que o Servidor esta
HOST = ''     	       # Endereco IP do Servidor
jogadores = []
ganhou = "8"
perdeu = "7"
esperando = "3"
iniciarJogo = "1"
outroJogando = "4"
fazerJogada = "2"
acabaramJogadas = "0"
empate = "5"

def server():
    #Abrindo um socket UDP na porta 5000
    orig = (HOST, PORT)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(orig)

    while True:
        #recebi dados
        data, address = sock.recvfrom(MAX_BYTES) # Recebi dados do socket

        #print(address, text)
        tratador = ThreadTratador(sock, address)
        tratador.start()
        jogadores.append(tratador)

        if len(jogadores) != 2:
            text = "3"  # Esperando outro jogadorse conectar
            data = text.encode(ENCODE)  # Codifica para BASE64 os dados
            sock.sendto(data, jogadores[0].address)  # Enviando dados

        else:
            text = iniciarJogo
            data = text.encode(ENCODE)  # Codifica para BASE64 os dados
            sock.sendto(data, jogadores[0].address)  # Enviando dados
            sock.sendto(data, jogadores[1].address)  # Enviando dados

            estaJogando = int(0)
            estaParado = int(1)
            aux = ''
            gameover = 0
            while gameover == 0:
                text = outroJogando
                data = text.encode(ENCODE)  # Codifica para BASE64 os dados
                sock.sendto(data, jogadores[estaParado].address)  # Enviando dados

                text = fazerJogada
                data = text.encode(ENCODE)  # Codifica para BASE64 os dados
                sock.sendto(data, jogadores[estaJogando].address)  # Enviando dados

                data, address = sock.recvfrom(MAX_BYTES)  # Recebi dados do socket
                text = data.decode(ENCODE)
                xy = text.split(",")
                print("X:"+xy[0]+" Y:"+xy[1])
                text = jogadores[estaParado].jogada(int(xy[0]), int(xy[1]))
                print(text)

                data = text.encode(ENCODE)  # Codifica para BASE64 os dados
                sock.sendto(data, jogadores[estaJogando].address)  # Enviando dados

                if jogadores[estaParado].bn.acertos == 2:
                    text = ganhou
                    data = text.encode(ENCODE)  # Codifica para BASE64 os dados
                    sock.sendto(data, jogadores[estaJogando].address)  # Enviando dados

                    text = perdeu
                    data = text.encode(ENCODE)  # Codifica para BASE64 os dados
                    sock.sendto(data, jogadores[estaParado].address)  # Enviando dados

                    gameover = 1

                elif jogadores[estaJogando].bn.numMaximoJogadas == 0 and jogadores[estaParado].bn.numMaximoJogadas == 0:

                    if jogadores[estaJogando].bn.acertos > jogadores[estaParado].bn.acertos:
                        data = ganhou.encode(ENCODE)  # Codifica para BASE64 os dados
                        sock.sendto(data, jogadores[estaJogando].address)  # Enviando dados

                        data = perdeu.encode(ENCODE)  # Codifica para BASE64 os dados
                        sock.sendto(data, jogadores[estaParado].address)  # Enviando dados

                    elif jogadores[estaJogando].bn.acertos < jogadores[estaParado].bn.acertos:
                        data = perdeu.encode(ENCODE)  # Codifica para BASE64 os dados
                        sock.sendto(data, jogadores[estaJogando].address)  # Enviando dados

                        data = ganhou.encode(ENCODE)  # Codifica para BASE64 os dados
                        sock.sendto(data, jogadores[estaParado].address)  # Enviando dados

                    else:
                        data = empate.encode(ENCODE)  # Codifica para BASE64 os dados
                        sock.sendto(data, jogadores[estaJogando].address)  # Enviando dados

                        data = empate.encode(ENCODE)  # Codifica para BASE64 os dados
                        sock.sendto(data, jogadores[estaParado].address)  # Enviando dados

                    gameover = 1

                elif jogadores[estaParado].bn.numMaximoJogadas == 0:
                    text = "0"
                    data = text.encode(ENCODE)  # Codifica para BASE64 os dados
                    sock.sendto(data, jogadores[estaJogando].address)  # Enviando dados


                aux = estaJogando
                estaJogando = estaParado
                estaParado = aux


class ThreadTratador(threading.Thread):

    def __init__(self, a, b):
        threading.Thread.__init__(self)
        self.sock = a
        self.address = b
        self.bn = BatalhaNaval.BatalhaNaval()

    def jogada(self, x, y):
        return self.bn.jogada(x, y)
