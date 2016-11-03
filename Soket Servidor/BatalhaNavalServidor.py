import socket
from datetime import datetime

ENCODE = "UTF-8"
MAX_BYTES = 65535
PORT = 5000            # Porta que o Servidor esta
HOST = ''     	       # Endereco IP do Servidor
response = ''
class BatalhaNavalServidor(object):
	
	def __init__(self):
		self.matriz = [ [ 0 for j in range(5) ] for i in range(5)]
		self.set_navio(2,3)
		self.set_navio(1,3)
		self.set_navio(0,3)
		self.set_navio(3,0)
		self.set_navio(4,1)
		self.set_navio(3,1)
		self.set_navio(4,4)
		self.numeroDeJogadas = 10
		self.jogadas =  []
		

	def set_navio(self, linha, coluna):
		self.matriz[linha][coluna] = 'E'

	def jogada(self, linha, coluna):
		if self.numeroDeJogadas > 0:
			if self.matriz[linha][coluna] == 'E':
				print('Acerto')
				self.matriz[linha][coluna] = 'M'
				self.jogadas.append(linha)
				self.jogadas.append(coluna)
				self.numeroDeJogadas = self.numeroDeJogadas - 1
				return "Acerto \n"

			else:
				print('Erro')
				self.numeroDeJogadas = self.numeroDeJogadas - 1
				return "Erro.\n"
		else:
			print("Você não possui mais jogadas! Fim de jogo.")

	def retornaJogadas(self):
		return self.jogadas

	


def server():
    #Abrindo um socket UDP na porta 5000
    orig = (HOST, PORT)																
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(orig)
    servidor = BatalhaNavalServidor()

    while True:
        #recebi dados
        data, address = sock.recvfrom(MAX_BYTES) # Recebi dados do socket
        text = data.decode(ENCODE) # Convertendo dados de BASE64 para UTF-8

        linha = int(text[0])
        coluna = int(text[1])
        
        text  = servidor.jogada(linha, coluna)
        #Envia resposta
       
        data = text.encode(ENCODE) # Codifica para BASE64 os dados 
        sock.sendto(data, address) # Enviando dados	

    #Fechando Socket
    sock.close()

