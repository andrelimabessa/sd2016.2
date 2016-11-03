import socket
from datetime import datetime

ENCODE = "UTF-8"
HOST = '127.0.0.1'   # Endereco IP do Servidor
PORT = 5000          # Porta que o Servidor esta
MAX_BYTES = 65535    # Quantidade de Bytes a serem ser recebidos
linhaColuna = []


class BatalhaNavalCliente(object):

    def __init__(self):
        self.numeroDeJogadas = 10
        self.jogadas =  []

    def salvaJogadas(self):

        jogadasRealizadas = open("jogadas.txt", "w")

        contadorUm = 0
        contadorDois = 1

        for x in range(len(self.jogadas)//2):
                stringASerSalva = str(str(self.jogadas[contadorUm]) + str(self.jogadas[contadorDois]))
                jogadasRealizadas.write("%s" % stringASerSalva)
                

                contadorUm = contadorUm +2
                contadorDois = contadorDois +2
        jogadasRealizadas.close

    def retornaJogadas(self):
        return self.jogadas

    def executa(self):
        arq = open("jogadas.txt", "r")

        for linha in arq:
            self.jogadas
            variavel = linha
            self.jogadas.append(int(variavel))

        arq.close()


def client():
    confimador = True
    contadorUm = 0
    contadorDois = 1
    cliente = BatalhaNavalCliente()

    cliente.executa()
    
    if len(cliente.jogadas) >0:
        palavra = cliente.jogadas[0]
        metade = len(str(palavra))//2
        
        for x in range(0,int(metade + 1)):
            #self.jogadasInicial(cliente.jogadas[contadorUm], cliente.jogadas[contadorDois])

            jogada = str(palavra)[contadorUm]
            jogadaDois = str(palavra)[contadorDois]

            jogadaString = str(jogada + jogadaDois)
            data = jogadaString.encode(ENCODE)


            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            dest = (HOST, PORT)
            sock.sendto(data, dest)

            data, address = sock.recvfrom(MAX_BYTES)
            text = data.decode(ENCODE)
            print(text)
            cliente.numeroDeJogadas = cliente.numeroDeJogadas - 1
            print("Você ainda possui " + str(cliente.numeroDeJogadas) + " jogadas")
            contadorDois = contadorUm + 1
            contadorUm = contadorUm + 1


    while confimador:
        if cliente.numeroDeJogadas == 0:
                print("Seu jogo acabou")
                confimador = false

        text = input("Digite uma Linha:\n")   		    # Recebe dados
        jogada = text + input("Digite uma Coluna:\n")
        linha = int(jogada[0])
        coluna = int(jogada[1])
        cliente.jogadas.append(linha)
        cliente.jogadas.append(coluna)
        cliente.salvaJogadas()
        data = jogada.encode(ENCODE)				    # Codifica para BASE64 os dados de entrada	
        #Envio de dados
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Inicializar um socket UDP
        dest = (HOST, PORT)                                     # Define IP de origem e Porta de destino  
        sock.sendto(data, dest)                                 # Envia os dados para o destino

        #Resposta de envio ao servidor
        data, address = sock.recvfrom(MAX_BYTES)                # Recebendo dados
        text = data.decode(ENCODE)
        cliente.numeroDeJogadas = cliente.numeroDeJogadas - 1
        print("Você ainda possui" + str(cliente.numeroDeJogadas))    
        print(text)                          # Convertendo dados de BASE64 para UTF-8
