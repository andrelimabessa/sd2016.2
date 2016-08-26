import os
import random
import pickle
import pandas as pd
from prettytable import PrettyTable

class BatalhaNaval(object):
  
  VERSAO = "0.2"
  SAVEFILE = "savefile.dat"
  
  linhas = 5
  colunas = 5
  
  jogadasRestantes = 15
  jogadasEfetuadas = ""
  maxBarcos = 5
  numBarcosAtingidos = 0
  
  tabuleiro = [[]]

  pecas = ["0", "1", "X"] # 0 - Água; 1 - Barco; X - Atingido
  
  def converteColuna(self, col):
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
    
  def imprimeTabuleiro(self):
    print("-=-=-=-=-=-=-=-=-=-=-=-=\tTabuleiro\t-=-=-=-=-=-=-=-=-=-=-=-=\n\n")
    print(pd.DataFrame(self.tabuleiro, columns=['A', 'B', 'C', 'D', 'E']))
    self.pressioneQualquer()
  
  def jogar(self):
    perdeu = 0
    
    while (self.jogadasRestantes > 0):
      self.limpaTela()
      
      print("\t\t\t\t\tBarcos atingidos: " + str(self.numBarcosAtingidos))
      print("\t\t\t\t\tJogadas restantes: " + str(self.jogadasRestantes))
      print("\t\t\t\t\tJogadas efetuadas:" + str(self.jogadasEfetuadas) + "\n\n")
      col = input("Digite a coluna que sera atingida(a, b, c, d ou e): ")
      pos = col
      col = self.converteColuna(col)
      lin = int(input("Digite a linha que sera atingida(0, 1, 2, 3 ou 4): "))
      pos = pos + str(lin)
          
      try:
        peca = self.tabuleiro[lin][col]
      except:
        print("Posicao invalida!")
        self.pressioneQualquer()
        continue
      
      self.jogadasEfetuadas = self.jogadasEfetuadas + " " + pos
      print("\n\nAtirando na posicao " + pos + "!\n")
      
      if (peca == 'X'):
        print("Ops, ja destruimos esse barco...")
      elif (int(peca) == 0):
        print("Ahh, aqui tem apenas agua...")
        self.jogadasEfetuadas = self.jogadasEfetuadas + "(O)"
      elif (int(peca) == 1):
        print("Atingimos um barco!")
        self.numBarcosAtingidos = self.numBarcosAtingidos + 1
        self.tabuleiro[lin][col] = 'X'
        self.jogadasEfetuadas = self.jogadasEfetuadas + "(X)"
        if (self.numBarcosAtingidos == 0):
          print("Destruimos todos os barcos, voce venceu!\n\n")
          break
      
      self.jogadasRestantes = self.jogadasRestantes - 1
      
      if (self.jogadasRestantes == 0):
        perdeu = 1
        print("Nao restam mais jogadas, voce perdeu!\n\n")
        self.pressioneQualquer()
        break
      
      op = input("\nDeseja continuar o jogo(s/n)? ")
      if (op.lower() == 's'):
        continue
      elif (op.lower() == 'n'):
        op = input("Salvar o jogo(s/n)? ")
        if (op.lower() == 's'):
          self.salvaJogo()
          break
        elif (op.lower() == 'n'):
          perdeu = 1
          break
    
    if ((perdeu == 1) or (self.numBarcosAtingidos == 0)):
      self.imprimeTabuleiro()
    
    self.mostraMenu()  

  def limpaTela(self):
    if (os.name == 'nt'):
      _=os.system("cls")
    else:
      _=os.system("clear")
    
  def mostraMenu(self):
    self.limpaTela()
    print("Batalha Naval - " + self.VERSAO + "\n\n")
    print("1 - Novo Jogo")
    print("2 - Continuar Jogo Anterior")
    print("9 - Sair")
    option = int(input("\nEscolha uma opcao: "))
    if (option == 1):
      self.tabuleiro = [[]]
      self.iniciaTabuleiro()
      self.jogar()
    elif (option == 2):
      if (os.path.exists(self.SAVEFILE)):
        self.restauraJogo()
      else:
        print("Arquivo savefile.dat nao encontrado, iniciando novo jogo!")
        self.pressioneQualquer()
        self.tabuleiro = [[]]
        self.iniciaTabuleiro()
      self.jogar()
    elif (option == 9):
      print("Bye!\n")
      quit()
    else:
      print("Opcao invalida!\n")
      self.mostraMenu()

  def pressioneQualquer(self):
    input("\n\nPressione qualquer tecla para continuar...")
   
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
      self.pressioneQualquer()