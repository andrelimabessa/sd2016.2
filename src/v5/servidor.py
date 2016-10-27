# coding: utf-8
from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer

from datetime import datetime
from batalhanaval import BatalhaNaval

class Servidor():
	@staticmethod
	def getInstance():
		if Servidor.__instance is None:
			Servidor.__instance = Servidor()
		return Servidor.__instance


	"""docstring for ClassName"""
	def __init__(self):
		self.jogo = BatalhaNaval(5, 5)		

	__instance = None

	def iniciar(self):
		print("Servidor iniciado")

	def incluirJogador(self, nick):
		resultado = self.jogo.incluirJogador(nick)
		print("Jogadores OnLine: " + str(self.jogo.getQuantidadeJogador()))

		return "sucesso"		

	def atirar(self, nick, i, j):
		if self.jogo.possuiJogadaRestante(nick):
			resultado = self.jogo.atirar(nick, int(i), int(j))
			if resultado == 0:
				mensagem = self.getMensagem("204")
			elif resultado == 1:
				mensagem = self.getMensagem("200")
			elif resultado == 2:
				mensagem = self.getMensagem("201")
			else:
				mensagem = "Código não encontrado"

			return mensagem
		else:
			mensagem = self.getMensagem('203')
			return mensagem
	    
	def getMensagem(self, codigo):
		if codigo == "200":        
			return "\n!!!!!!!!!!!!!!!!!!!!!!!!\n!!!!!!  Booooom  !!!!!!!\n!!!!!!!!!!!!!!!!!!!!!!!!\n"
		if codigo == "201":
			return "\n~~~~~~~~~~~~~~~~~~~~~~~~\n~~~~~~~   Água   ~~~~~~~\n~~~~~~~~~~~~~~~~~~~~~~~~\n"
		if codigo == "202":
			return "** Posição além do tamanho do tabuleiro **"        
		if codigo == "203":
			return "----- Sem jogada restante ------\n ----- Voce perdeu ------"
		if codigo == "204":
			return "----- Posição já verificada ------"

def incluirJogador(nick):
	batalha = Servidor().getInstance()
	resultado = batalha.incluirJogador(nick)	
	return resultado

def atirar(nick, i, j):
	batalha = Servidor().getInstance()
	print("tiro: ", nick, i, j)
	resultado = batalha.atirar(nick, i, j)
	return resultado
	
def server():
	serverRPC = SimpleJSONRPCServer(('localhost', 7002))
	serverRPC.register_function(incluirJogador)
	serverRPC.register_function(atirar)
	print("Starting server")
	serverRPC.serve_forever()
