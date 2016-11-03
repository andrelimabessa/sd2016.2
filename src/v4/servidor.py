# coding: utf-8
import zmq
import time
import sys
import random

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
		self.jogo.carregarJogo()

	def iniciar(self):
		self.iniciarEscuta()
	
	def iniciarEscuta(self):

		# trecho extraído do queue_server
		try:
			port = "5560"
			context = zmq.Context()
			socket = context.socket(zmq.REP)
			socket.connect("tcp://localhost:%s" % port)
			server_id = random.randrange(1,10005)
			while True:
				#  Espera pela próxima requisição do cliente
				message = socket.recv()
				print("Recebi requisição de : ", message)
				time.sleep (1)				

				# executa comando
				resultado = self.tratar_conexao(socket, message)

				## salva jogo
				self.jogo.salvarJogo()
				
				# envia requisição com retono de comando
				data = resultado.encode("UTF-8")
				socket.send(data)
				
		except:
			for val in sys.exc_info():
				print(val)

	def tratar_conexao(self, sock, data):
		text = data.decode(ENCODE)
		
		resultado = self.executarComando(text)

		# define código de erro para retorno
		if not (resultado is None):
			text = resultado
		else:			
			text = "Quantidade de bytes enviados: " + str(len(data))
		return text

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