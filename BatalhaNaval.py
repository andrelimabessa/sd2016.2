import random
import pickle
import pandas as pd
from prettytable import PrettyTable

class BatalhaNaval(object):
  
  linhas = 5
  colunas = 5
  numBarcos = 3
  tabuleiro = [[]]
  maxJogadas = 10
  saveFile = "savefile.dat"
  pecas = ["0", "1", "2"] # 0 - Água; 1 - Barco; 2 - Atingido
  
  def iniciaTabuleiro(self):
    barcosInseridos = 0
    for i in range(self.linhas):
      self.tabuleiro.append([])
      for j in range(self.colunas):
        x = random.randrange(2)
        if (x == 1):
          barcosInseridos = barcosInseridos + 1
          if (barcosInseridos > self.numBarcos):
            x = 0
        self.tabuleiro[i].append(self.pecas[x])
    
  def imprimeTabuleiro(self):
    print("-=-=-=-=-=-=-=-=-=-=-=-=\tTabuleiro\t-=-=-=-=-=-=-=-=-=-=-=-=\n\n")
    print(pd.DataFrame(self.tabuleiro, columns=['A', 'B', 'C', 'D', 'E']))
    
  def mostraMenu(self):
    print("Batalha Naval - 0.1\n\n")
    print("1 - Novo Jogo")
    print("2 - Continuar Jogo Anterior")
    print("3 - Salvar Jogo Atual")
    print("9 - Sair")
    option = int(input("Escolha uma opcao: "))
    if (option == 1):
      print("Jogar!\n")
      self.tabuleiro = [[]]
      self.iniciaTabuleiro()
      self.jogar()
      self.imprimeTabuleiro()
      self.mostraMenu()
    elif (option == 2):
      print("Continuar jogo!\n")
      self.restauraJogo()
      self.imprimeTabuleiro()
      self.mostraMenu()
    elif (option == 3):
      self.salvaJogo()
      print("Jogo salvo!\n")
      self.mostraMenu()
    elif (option == 9):
      self.salvaJogo()
      print("Bye!\n")
      quit()
    else:
      print("Opcao invalida!\n")
      self.mostraMenu()
  
  def jogar(self):
    print("Jogo!")
    #self.imprimeTabuleiro()
    
  def salvaJogo(self):
    with open(self.saveFile, 'wb') as f:
      pickle.dump(self.tabuleiro, f)
    
  def restauraJogo(self):
    with open(self.saveFile, 'rb') as f:
      self.tabuleiro = pickle.load(f)