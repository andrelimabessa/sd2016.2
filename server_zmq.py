import socket
import sys
import pickle
import random
import zmq
from BatalhaNaval import BatalhaNaval

batalhaServer = BatalhaNaval()
host = 'localhost'
port = "5560"

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
 
context = zmq.Context()
	  
# Create a ZMQ socket
sock = context.socket(zmq.REP)
sock.connect("tcp://localhost:%s" % port)
server_id = random.randrange(1,10005)

while True:  
    try:
        dict = batalhaServer.recebeComandoZMQ(sock)
        cmd = dict["cmd"]
        print(cmd)
        data = dict["data"]
        print('received "%s"' % cmd, file=sys.stderr)
        if cmd:
            print('sending data back to the client', file=sys.stderr)
            returnData = processaComando(cmd, data)
            batalhaServer.enviaComandoZMQ(sock, "", returnData)
        else:
            print('no more cmd from client', file=sys.stderr)
            break
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise
    finally:
        # Clean up the connection
        #connection.close()
        print('Comando processado')