import zmq
import sys
import random




ENCODE = "UTF-8"



def client():
    port = "5559"
    context = zmq.Context()
    print("Conectando com o servidor...")
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:%s" % port)
    client_id = random.randrange(1, 10005)
    gameOver = 0
    while gameOver == 0:
        print ("1 - Novo Jogo")
        print("2 - Fazer jogada")
        text = input("Digite uma opcao:\n")  # Recebe dados
        data = text.encode(ENCODE)  # Codifica para BASE64 os dados de entrada
        socket.send(data)  # Envia os dados para o destino

        # Resposta de envio ao servidor
        text = socket.recv()
        if int(text) == 0:
            text = "The End, inicie um novo jogo!"
            gameOver = 1

        elif int(text) == 1:
            text = "Novo Jogo Iniciado"

        elif int(text) == 2:
            x = input("Digite a posicao do eixo X:")
            y = input("Digite a posicao do eixo Y:")
            text = str(x)+","+str(y)
            data = text.encode(ENCODE)
            socket.send(data)  # Envia os dados para o destino

            # Resposta de envio ao servidor
            data = socket.recv()
            text = data.decode(ENCODE)

        print("Saida")
        print("\n\n"+str(text)+"\n")  # Imprime texto e endereços
