import os
import random
import pickle
import pandas as pd
import socket
import sys
import struct
import time
from prettytable import PrettyTable

class BatalhaNaval(object):
  
  SAVEFILE = "savefile.dat"
  VERSAO = "0.2"
  linhas = 5
  colunas = 5
  
  jogadasRestantes = 15
  jogadasEfetuadas = ""
  maxBarcos = 5
  numBarcosAtingidos = 0
  
  tabuleiro = [[]]

  pecas = ["0", "1", "X"] # 0 - Água; 1 - Barco; X - Atingido
  
  def conectaServidor(self, sock, host, port):
    # Connect the socket to the port where the server is listening
    server_address = (host, port)
    print('connecting to {0} port {1}'.format(host, port), file=sys.stderr)
    sock.connect(server_address)
    
  def desconectaServidor(self, sock):
    sock.close()
    
  def enviaComando(self, sock, cmd, data):
    data = pickle.dumps(dict(cmd=cmd, data=data))
    print(cmd)
    sock.sendall(data)
    
  def recebeComando(self, sock):
    #make socket non blocking
#    sock.setblocking(0)
    connData = sock.recv(8192)
    
    try:
      data = pickle.loads(connData)
    except EOFError:
      return {}
    
    return data
    
#  def recebeComando(self, sock, timeout):
#      #make socket non blocking
#      sock.setblocking(0)
#       
#      #total data partwise in an array
#      total_data=bytes()
#      #data='';
#       
#      #beginning time
#      begin=time.time()
#      while 1:
#          #if you got some data, then break after timeout
#          if total_data and time.time()-begin > timeout:
#              break
#           
#          #if you got no data at all, wait a little longer, twice the timeout
#          elif time.time()-begin > timeout*2:
#              break
#           
#          #recv something
#          try:
#              data = pickle.loads(sock.recv(8192))
#              print(data)
#              if data:
#                  total_data = data
#                  #change the beginning time for measurement
#                  begin = time.time()
#              else:
#                  #sleep for sometime to indicate a gap
#                  time.sleep(0.1)
#          except:
#              pass
#       
#      #join all parts to make final string
#      print(total_data)
#      return total_data
 
  def iniciaTabuleiro(self):
    barcosInseridos = 0
    for i in range(self.linhas):
      self.tabuleiro.append([])
      for j in range(self.colunas):
        x = random.randrange(2)
        if (x == 1):
          barcosInseridos = barcosInseridos + 1
          if (barcosInseridos > self.maxBarcos):
            x = 0
        self.tabuleiro[i].append(self.pecas[x])
  
  def resetaTabuleiro(self):
    self.tabuleiro = [[]]
    
  def imprimeTabuleiro(self):
    print("-=-=-=-=-=-=-=-=-=-=-=-=\tTabuleiro\t-=-=-=-=-=-=-=-=-=-=-=-=\n\n")
    print((pd.DataFrame(self.tabuleiro, columns=['A', 'B', 'C', 'D', 'E']))) 
   
  def restauraJogo(self):
    with open(self.SAVEFILE, 'rb') as f:
      savedata = pickle.load(f)
      self.jogadasEfetuadas = savedata["jogadasEfetuadas"]
      self.jogadasRestantes = savedata["jogadasRestantes"]
      self.numBarcosAtingidos = savedata["numBarcosAtingidos"]
      self.tabuleiro = savedata["tabuleiro"]
      
  def salvaJogo(self):
    with open(self.SAVEFILE, 'wb') as f:
      pickle.dump(dict(numBarcosAtingidos=self.numBarcosAtingidos, jogadasEfetuadas=self.jogadasEfetuadas, jogadasRestantes=self.jogadasRestantes, tabuleiro=self.tabuleiro), f)
      print("Jogo salvo!")