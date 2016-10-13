import socket
import sys
import pickle
import threading
from BatalhaNaval import BatalhaNaval

batalhaServer = BatalhaNaval()
host = 'localhost'
port = 17543

def geraTabuleiro():
  batalhaServer.resetaTabuleiro()
  batalhaServer.iniciaTabuleiro()
  batalhaServer.imprimeTabuleiro()
  return batalhaServer.tabuleiro
  
def processaComando(cmd, data):
    if (cmd == 'geraTabuleiro'):
      print("Gerando tabuleiro no servidor")
      geraTabuleiro()
      return batalhaServer.tabuleiro
    elif (cmd == 'desconectaServidor'):
      sock.close()
    else:
      print("Comando invalido!\n")

def serverThread():
	# Create a TCP/IP socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

	# Bind the socket to the port
	server_address = (host, port)
	print('starting up on %s port %s' % server_address, file=sys.stderr)
	sock.bind(server_address)
	# Listen for incoming connections
	sock.listen(4)
	# Wait for a connection
	print('waiting for a connection', file=sys.stderr)
	while True:
		connection, client_address = sock.accept()
		print('connection from', client_address, file=sys.stderr)
		# Criação de thread procedural
		t = threading.Thread(target=tratarConexao, args=tuple([sock, dict, client_address, connection]))
		t.start()
			
def tratarConexao(sock, dict, address, connection):
  # Receive the data in small chunks and retransmit it
  dict = batalhaServer.recebeComando(connection)
  cmd = dict["cmd"]
  print(cmd)
  data = dict["data"]
  print('received "%s"' % cmd, file=sys.stderr)
  if cmd:
    print('sending data back to the client', file=sys.stderr)
    returnData = processaComando(cmd, data)
    batalhaServer.enviaComando(connection, "", returnData)
  else:
    print('no more cmd from', client_address, file=sys.stderr)

			
class ThreadTratador(threading.Thread):

    def __init__(self, a, b, c):
        threading.Thread.__init__(self)
        self.sock = a
        self.dict = b
        self.address = c
        self.connection = d

    def run(self):
        tratarConexao(self.sock, self.data, self.address)
		
serverThread()