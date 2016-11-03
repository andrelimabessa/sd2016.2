import os
import random
import pickle
import socket
import sys
import zmq
from BatalhaNaval import BatalhaNaval

host = 'localhost'
port = 5559
context = zmq.Context()
# Create a TCP/IP socket
sock = context.socket(zmq.REQ)
batalhaClient = BatalhaNaval()

def converteColuna(col):
  if (col.lower() == 'a'):
    return 0
  elif (col.lower() == 'b'):
    return 1
  elif (col.lower() == 'c'):
    return 2
  elif (col.lower() == 'd'):
    return 3
  elif (col.lower() == 'e'):
    return 4
  
def jogar():
  perdeu = 0
  
  while (batalhaClient.jogadasRestantes > 0):
    limpaTela()
    
    print(("\t\t\t\t\tBarcos atingidos: " + str(batalhaClient.numBarcosAtingidos)))
    print(("\t\t\t\t\tJogadas restantes: " + str(batalhaClient.jogadasRestantes)))
    print(("\t\t\t\t\tJogadas efetuadas:" + str(batalhaClient.jogadasEfetuadas) + "\n\n"))
    col = input("Digite a coluna que sera atingida(a, b, c, d ou e): ")
    pos = col
    col = converteColuna(col)
    lin = int(input("Digite a linha que sera atingida(0, 1, 2, 3 ou 4): "))
    pos = pos + str(lin)
        
    try:
      peca = batalhaClient.tabuleiro[lin][col]
    except:
      print("Posicao invalida!")
      pressioneQualquer()
      continue
    
    batalhaClient.jogadasEfetuadas = batalhaClient.jogadasEfetuadas + " " + pos
    print(("\n\nAtirando na posicao " + pos + "!\n"))
    
    if (peca == 'X'):
      print("Ops, ja destruimos esse barco...")
    elif (int(peca) == 0):
      print("Ahh, aqui tem apenas agua...")
      batalhaClient.jogadasEfetuadas = batalhaClient.jogadasEfetuadas + "(O)"
    elif (int(peca) == 1):
      print("Atingimos um barco!")
      batalhaClient.numBarcosAtingidos = batalhaClient.numBarcosAtingidos + 1
      batalhaClient.tabuleiro[lin][col] = 'X'
      batalhaClient.jogadasEfetuadas = batalhaClient.jogadasEfetuadas + "(X)"
      if (batalhaClient.numBarcosAtingidos == 0):
        print("Destruimos todos os barcos, voce venceu!\n\n")
        break
    
    batalhaClient.jogadasRestantes = batalhaClient.jogadasRestantes - 1
    
    if (batalhaClient.jogadasRestantes == 0):
      perdeu = 1
      print("Nao restam mais jogadas, voce perdeu!\n\n")
      pressioneQualquer()
      break
    
    op = input("\nDeseja continuar o jogo(s/n)? ")
    if (op.lower() == 's'):
      continue
    elif (op.lower() == 'n'):
      op = input("Salvar o jogo(s/n)? ")
      if (op.lower() == 's'):
        batalhaClient.salvaJogo()
        break
      elif (op.lower() == 'n'):
        perdeu = 1
        break
  
  if ((perdeu == 1) or (batalhaClient.numBarcosAtingidos == 0)):
    batalhaClient.imprimeTabuleiro()
    pressioneQualquer()
  
  mostraMenu()   
  
def limpaTela():
  if (os.name == 'nt'):
    _=os.system("cls")
  else:
    _=os.system("clear")  

def mostraMenu():
  limpaTela()
  print(("Batalha Naval - " + batalhaClient.VERSAO + "\n\n"))
  print("1 - Novo Jogo")
  print("2 - Continuar Jogo Anterior")
  print("9 - Sair")
  option = int(input("\nEscolha uma opcao: "))
  if (option == 1):
    batalhaClient.resetaTabuleiro()
    batalhaClient.enviaComandoZMQ(sock, "geraTabuleiro", "")
    dict = batalhaClient.recebeComando(sock)
    print(dict)
    batalhaClient.tabuleiro = dict["data"]
    jogar()
  elif (option == 2):
    if (os.path.exists(batalhaClient.SAVEFILE)):
      batalhaClient.restauraJogo()
    else:
      print("Arquivo savefile.dat nao encontrado, iniciando novo jogo!")
      pressioneQualquer()
      batalhaClient.resetaTabuleiro()
      batalhaClient.iniciaTabuleiro()
    jogar()
  elif (option == 9):
    print("Bye!\n")
    quit()
  else:
    print("Opcao invalida!\n")
    mostraMenu()    

def pressioneQualquer():
  input("\n\nPressione qualquer tecla para continuar...")

#print(batalhaClient.VERSAO)
#batalhaClient.iniciaTabuleiro()
#batalhaClient.imprimeTabuleiro()
client_id = random.randrange(1,10005)
batalhaClient.conectaServidorZMQ(sock, host, port)
mostraMenu()