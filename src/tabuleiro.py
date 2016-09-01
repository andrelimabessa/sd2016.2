import posicao

class Tabuleiro(object):
	def __init__(self, tamanho):
		self.tamanho = tamanho		
		self.matriz = [ [ posicao.Posicao() for j in range(tamanho) ] for i in range(tamanho)]	
		
	def inicializar(self):
		self.matriz[0][3].conteudo = "B"
		self.matriz[1][1].conteudo = "B"
		self.matriz[2][4].conteudo = "B"
		self.matriz[3][4].conteudo = "B"		
	
	def definirBarco(self, i, j):
		self.matriz[i][j].conteudo = "B"
		
	def definirAcerto(self, i, j):
		self.matriz[i][j].acerto = "S"
		
	def marcarPosicaoVerificada(self, i, j):
		self.matriz[i][j].verificada = "S"
	
	def obterPosicoesVerificadas(self):				
		lista = []
		for j in range(self.tamanho): 
			for i in range(self.tamanho): 	
				if self.matriz[i][j].verificada == "S":					
					lista.append({"linha": i, "coluna":j})			
		return lista		

	def obterPosicoesAcerto(self):				
		lista = []
		for j in range(self.tamanho): 
			for i in range(self.tamanho): 	
				if self.matriz[i][j].acerto == "S":					
					lista.append({"linha": i, "coluna":j})
		return lista			
	
	def obterBarcos(self):
		lista = []
		for i in range(self.tamanho): 
			for j in range(self.tamanho): 	
				if self.matriz[i][j].conteudo == "B":
					lista.append({"linha": i, "coluna":j})
		return lista
	
	def verificarJogada(self, i, j):
		if self.tamanho < i+1:
			raise Exception("Tamanho máximo para (i) excedido. Máximo:" + str(self.tamanho-1))
			
		if self.tamanho < j+1:
			raise Exception("Tamanho máximo para (j) excedido. Máximo: " + str(self.tamanho-1))
		
		if self.matriz[i][j].verificada == "S":		
			print("\n*** Posição já verificada ***")
			return False;
		else:
			self.matriz[i][j].verificada = "S" ## marca posição como verificada
			
			if self.matriz[i][j].conteudo == "B":
				self.matriz[i][j].acerto = "S"
				print("")
				print("!!!!!!!!!!!!!!!!!!!!!!!!")
				print("!!!!!!  Booooom  !!!!!!!")
				print("!!!!!!!!!!!!!!!!!!!!!!!!")
				print("")
			else:
				self.matriz[i][j].acerto = "N"
				print("")
				print("~~~~~~~~~~~~~~~~~~~~~~~~")
				print("~~~~~~~   Água   ~~~~~~~")
				print("~~~~~~~~~~~~~~~~~~~~~~~~")
				print("")
			return True;