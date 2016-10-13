# coding: utf-8
import socket
import threading
from datetime import datetime
from batalhanaval import BatalhaNaval

ENCODE = "UTF-8"
MAX_BYTES = 65535
PORT = 5000            # Porta que o Servidor esta
HOST = ''     # Endereco IP do Servidor


class Servidor():
	"""docstring for ClassName"""
	def __init__(self):
		self.jogo = BatalhaNaval(5, 5)		

	def iniciar(self):
		self.iniciarEscuta()
	
	def iniciarEscuta(self):
    	#Abrindo uma porta UDP
		orig = (HOST, PORT)
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sock.bind(orig)
		while True:
            #recebe dados
			data, address = sock.recvfrom(MAX_BYTES)
     
            #Criação de thread orientada a objeto
			tratador = ThreadTratador(sock, data, address, self.jogo)
			tratador.start()			


class ThreadTratador(threading.Thread):

	def __init__(self, a, b, c, jogo):
		threading.Thread.__init__(self)
		self.sock = a
		self.data = b
		self.address = c
		self.jogo = jogo

	def run(self):
		self.tratar_conexao(self.sock, self.data, self.address)

	def tratar_conexao(self, sock, data, address):
		text = data.decode(ENCODE)
		
		resultado = self.executarComando(text)

		# define código de erro para retorno
		if not (resultado is None):
			text = resultado
		else:			
			text = "Quantidade de bytes enviados: " + str(len(data))			

		#Envia resposta
		data = text.encode(ENCODE)
		sock.sendto(data, address)

	# prepara e realiza requisão ao servidor
	# de acordo com o comando informado
	def executarComando(self, text):	
		
		retorno = ""
		valores = text.split(':')
		cmd = valores[0]		
		parametro = valores[1]

		# Inclusão de jogador
		## Comando exemplo: "nw:nick"
		if cmd == "nw":
			try:			
				resultado = self.jogo.incluirJogador(parametro)
				print("Jogadores OnLine: " + str(self.jogo.getQuantidadeJogador()))							
			except Exception as erro:
				# formata código de erro
				retorno = self.formatarErro("100")

		# Realiza tiro
		## Comando exemplo: "fi:nick:posicaoI-posicaoJ"
		if cmd == "fi":			
			posicoes = valores[2].split('-')

			if self.jogo.possuiJogadaRestante(parametro):
				try:
					resultado = self.jogo.atirar(parametro, int(posicoes[0]), int(posicoes[1]))

					if resultado == 0:
						retorno = self.formatarSucesso("204")
					elif resultado == 1:
						retorno = self.formatarSucesso("200")
					else: # resultado == 2:
						retorno = self.formatarSucesso("201")

				except Exception as e:											
					retorno = self.formatarSucesso("202")	
			else:
				retorno = self.formatarSucesso("203")

		return retorno

	# trata resposta de erro
	def formatarErro(self, codigo):		
		text = "ERR:" + codigo		
		return text

	# trata resposta de sucesso
	def formatarSucesso(self, codigo):		
		text = "COD:" + codigo		
		return text
