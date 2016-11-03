import socket
import sys
import pickle
import rpyc
sys.path.append("..")
from BatalhaNaval import BatalhaNaval

batalhaServer = BatalhaNaval()
host = 'localhost'
pt = 17544

class Batalha(rpyc.Service):

	def exposed_geraTabuleiro(self):
	  batalhaServer.resetaTabuleiro()
	  batalhaServer.iniciaTabuleiro()
	  batalhaServer.imprimeTabuleiro()
	  return batalhaServer.tabuleiro
	  
	def processaComando(self, cmd, data):
		if (cmd == 'geraTabuleiro'):
		  print("Gerando tabuleiro no servidor")
		  geraTabuleiro()
		  return batalhaServer.tabuleiro
		elif (cmd == 'desconectaServidor'):
		  sock.close()
		else:
		  print("Comando invalido!\n")

def serverThread():
	from rpyc.utils.server import ThreadedServer
	t = ThreadedServer(Batalha, port = pt)
	t.start()
		
serverThread()