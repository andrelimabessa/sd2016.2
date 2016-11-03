import BatalhaNaval
import zmq
import sys
import random

ENCODE = "UTF-8"


def limparLogs():
    arq = open("LogJogadas.txt", "w")
    arq.close()
    arq = open("LogTabuleiro.txt", "w")
    arq.close()


def server():
    a = BatalhaNaval.BatalhaNaval()
    jogoCarregado = True
    if not(a.existeJogoSalvo()):
        jogoCarregado = False
        a = ''

    try:
        port = "5560"
        context = zmq.Context()
        socket = context.socket(zmq.REP)
        socket.connect("tcp://localhost:%s" % port)
        server_id = random.randrange(1, 10005)
        while True:
            #  Espera pela próxima requisição do cliente
            text = socket.recv()

            if jogoCarregado:
                try:
                    int(text)
                    jogoCarregado = False
                except:
                    jogoCarregado = False
                    data = text.decode(ENCODE)
                    xy = data.split(",")

                    text = a.jogada(int(xy[0]), int(xy[1]))
                    data = text.encode(ENCODE)  # Codifica para BASE64 os dados
                    socket.send(data)  # Enviando dados
                    continue

            if int(text) == 1:
                limparLogs()
                a = BatalhaNaval.BatalhaNaval()
                # Envia resposta
                text = "1"
                data = text.encode(ENCODE)  # Codifica para BASE64 os dados
                socket.send(data)  # Enviando dados

            if int(text) == 2:
                text = "2"
                if a.numMaximoJogadas == 0:
                    a.limparLogs()
                    text = "0"
                    data = text.encode(ENCODE)  # Codifica para BASE64 os dados
                    socket.send(data)
                else:
                    data = text.encode(ENCODE)  # Codifica para BASE64 os dados
                    socket.send(data)

                    data = socket.recv()
                    text = data.decode(ENCODE)

                    xy = text.split(",")
                    text = a.jogada(int(xy[0]), int(xy[1]))
                    data = text.encode(ENCODE)  # Codifica para BASE64 os dados
                    socket.send(data)  # Enviando dados


    except:
        for val in sys.exc_info():
            print(val)

