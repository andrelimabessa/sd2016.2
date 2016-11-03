import socket
import sys
import pickle
sys.path.append("..")
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

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
timeout = 2

# Bind the socket to the port
server_address = (host, port)
print('starting up on %s port %s' % server_address, file=sys.stderr)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

# Wait for a connection
print('waiting for a connection', file=sys.stderr)
connection, client_address = sock.accept()
	
while True:
    try:
      print('connection from', client_address, file=sys.stderr)
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
        break
    except:
      raise
    #finally:
        # Clean up the connection
        #connection.close()