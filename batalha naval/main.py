import time
import random
import os


class Main():

	_tentativas = 5

	#constructor
	def __init__(self, matriz = None, tentativas = 5):
		self.tentativas = tentativas
		if (matriz is None):
			# 0 = agua
			# 1 = Bomba
			# 2 = Navio
			self.matriz = [ [ random.choice([0, 1, 2]) for j in range(5) ] for i in range(5)]
		else :
			self.matriz = matriz

		#print(self.get_matriz())

	def menu(self):
		resposta = input("1 - novo jogo \n2 - cotinuar de onde parou \n3 - sair: ")

		if(resposta == "2"):
			temp = self.lerAquivo()
			if(temp["tentativas"] is None):
				self.tentativas = self._tentativas
			else:
				self.tentativas = temp["tentativas"]
			if(temp["acertos"] is None):
				self.acertos = 0
			else:
				self.acertos = temp["acertos"]
			self.jogo()
		elif(resposta == 1):
			self.jogo()
		else:
			exit(0)

	def lerAquivo(self):
		try:
			arq = open("jogo.txt", "x")
		except FileExistsError:
			arq = open("jogo.txt", "r")
			conteudo = arq.readline()
			arq.close()
			array = conteudo.split(",")
			if(len(array) >= 2):
				print(array)
				jogoAnterior = {"tentativas" : int(array[0]), "acertos" : int(array[1])}
			else:
				jogoAnterior = {"tentativas" : None, "acertos" : None}
			
			return jogoAnterior

	def escreveArquivo(self):
		arq = open("jogo.txt", "w")
		arq.write(str(self.tentativas) + ","+str(self.acertos))
		arq.close()

	def get_matriz(self):
		return self.matriz

	def jogo(self):

		os.system('CLS')
		
		print("----- Batalha Naval -----")
		print("Digite a posiçao (x, y) do tabuleiro")
		print("Tentativas restantes: " + str(self.tentativas))
		print("Barcos atingidos: " + str(self.acertos))
		linha = input("Informe a linha de 1 a 5: ")
		coluna = input("Informe a coluna de 1 a 5: ")

		if(self.isInt(linha) and self.isInt(coluna)):
			print("")
		else:
		    print("Linha ou coluna devem ser numeros")
		    self.jogo()


		x = self.matriz[int(linha) - 1][int(coluna) - 1]

		if (x == 0):
			self.tentativas -= 1
			print("Água")
			if(self.tentativas < 0):
				self.game_over()
			else:
				self.continuarJogo()
		elif (x == 1):
			self.tentativas -= 1
			print("Bomba")
			if(self.tentativas < 0):
				self.game_over()
			else:
				self.continuarJogo()
		else:
			self.tentativas -= 1
			self.acertos += 1
			print("Acertou")
			if(self.tentativas < 0):
				self.game_over()
			else:
				self.continuarJogo()

	def game_over(self):
		print("1 - novo jogo")
		print("2 - Sair")

		x = input("O que você deseja fazer? ")

		if(int(x) == 1):
			self.tentativas = self._tentativas
			self.acertos = 0
			self.jogo()
		elif(int(x) == 2):
			exit(0)
		else:
			print("Opção inválida")
			self.game_over()

	def continuarJogo(self):
		print("Deseja continuar o jogo?")
		resposta = input("s - sim, n- não: ")

		if(resposta.upper() == "S"):
			self.jogo()
		elif(resposta.upper() == "N"):
			self.escreveArquivo()
			exit(0)
		else:
			print("Opção inválida")
			self.continuarJogo()

	def isInt(self, s):
	    try: 
	        int(s)
	        if(int(s) > 5):
	        	print("Posição inválida: Informe uma posição de 1 a 5")
	        	return False
	        return True
	    except ValueError:
	        return False