class BatalhaNaval(object):

	def __init__(self, numeroDeJogadas):
		self.matriz = [["~" for j in range(5)] for i in range(5)]
		self.numeroDeJogadas = numeroDeJogadas
		

	def initBarcos(self):
		self.matriz[0][1]="@"
		self.matriz[3][2]="@"
		self.matriz[2][4]="@"
		self.salvaLogDoTabuleiro(self.matriz)

	def salvaLogDeJogada(self, eixoX, eixoY):
		self.arq = open("LogDeJogadas.txt", "a")
		self.arq.write("X:"+str(eixoX)+"\n")
		self.arq.write("Y:"+str(eixoY)+"\n")
		self.arq.close()

	def limpaLog(self, log):
		self.arq = open(log, "w")
		self.arq.close()

	def salvaLogDoTabuleiro(self, matriz):
		self.arq = open("LogDoTabuleiro.txt", "w")
		self.arq.write(str(matriz))
		self.arq.close()

	def salvaLogNumJogadas(self, numeroDeJogadas):
		self.arq = open("LogNumeroDeJogadas.txt", "w")
		self.arq.write(str(numeroDeJogadas))
		self.arq.close()

	def jogada(self):
		self.numeroDeJogadas -= 1
		self.salvaLogNumJogadas(self.numeroDeJogadas)
		eixoX = int(input("Insira a coordenada do eixo X: "))
		eixoY = int(input("Insira a coordenada do eixo Y: "))
		self.salvaLogDeJogada(eixoX, eixoY)
		if self.matriz[eixoX][eixoY] == "@":
			self.matriz[eixoX][eixoY] = "*"
			self.salvaLogDoTabuleiro(self.matriz)
			print("Acertou o barco!")
		elif self.matriz[eixoX][eixoY] == "~":
			print("Acertou a agua!")
		else:
			print("Barco ja afundado.")