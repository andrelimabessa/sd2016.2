import random


class BatalhaNaval(object):

	def __init__(self, numeroDeJogadas):
		self.matriz = [["~" for j in range(5)] for i in range(5)]
		self.numeroDeJogadas = numeroDeJogadas
		if self.existeJogo():
			self.carregaPosicoesBarcos()
			self.carregaAcertos()
			self.carregaNumeroJogadas()
		else:
			self.initBarcos()

	def initBarcos(self):
		for i in range(3):
			eixoX = random.randint(0, 4)
			eixoY = random.randint(0, 4)
			if self.matriz[eixoX][eixoY] == "@":
				i -= 1
			else:
				self.matriz[eixoX][eixoY] = "@"
				self.salvaPosicoesDosBarcos(eixoX, eixoY)
			self.salvaLogDoTabuleiro(self.matriz)

# Salvar-----------------------------------------------------------

	def salvaLogDeAcerto(self, eixoX, eixoY):
		self.arq = open("LogDeAcertos.txt", "a")
		self.arq.write(str(eixoX) + "-" + str(eixoY) + "\n")
		self.arq.close()

	def salvaPosicoesDosBarcos(self, eixoX, eixoY):
		self.arq = open("LogPosicaoBarcos.txt", "a")
		self.arq.write(str(eixoX) + "-" + str(eixoY) + "\n")
		self.arq.close()

	def salvaLogDoTabuleiro(self, matriz):
		self.arq = open("LogDoTabuleiro.txt", "w")
		self.arq.write(str(matriz))
		self.arq.close()

	def salvaLogNumJogadas(self, numeroDeJogadas):
		self.arq = open("LogNumeroDeJogadas.txt", "a")
		self.arq.write(str(numeroDeJogadas)+"\n")
		self.arq.close()

# Jogada-----------------------------------------------------------------------------------

	def jogada(self):
		self.numeroDeJogadas -= 1
		self.salvaLogNumJogadas(self.numeroDeJogadas)
		print("Jogadas disponiveis: " + str(self.numeroDeJogadas + 1))
		eixoX = int(input("Insira a coordenada do eixo X: "))
		eixoY = int(input("Insira a coordenada do eixo Y: "))
		if self.matriz[eixoX][eixoY] == "@":
			self.matriz[eixoX][eixoY] = "*"
			self.salvaLogDoTabuleiro(self.matriz)
			self.salvaLogDeAcerto(eixoX, eixoY)
			print("Acertou o barco!")
		elif self.matriz[eixoX][eixoY] == "~":
			print("Acertou a agua!")
		else:
			print("Barco ja afundado.")

# Carregar----------------------------------------------------------------------------

	def existeJogo(self):
		arq = open("LogDoTabuleiro.txt", "r")
		if arq.readline() == "":
			existe = False
		else:
			existe = True
		return existe

	def carregaPosicoesBarcos(self):
		arq = open("LogPosicaoBarcos.txt", "r")
		for linha in arq:
			valor = linha.split("-")
			self.matriz[int(valor[0])][int(valor[1])] = "@"
		arq.close()

	def carregaAcertos(self):
		arq = open("LogDeAcertos.txt", "r")
		for linha in arq:
			valor = linha.split("-")
			self.matriz[int(valor[0])][int(valor[1])] = "*"
		arq.close()

	def carregaNumeroJogadas(self):
		arq = open("LogNumeroDeJogadas.txt", "r")
		for linha in arq:
			self.numeroDeJogadas = int(linha) + 1
		arq.close()

# Limpar------------------------------------------------------------------------------------------

	def limpaLog(self, log):
		self.arq = open(log, "w")
		self.arq.close()