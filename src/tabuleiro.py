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
	
	def obterPosicoesNaoVerificadas(self):
				
		lista = []
		for i in range(self.tamanho): 
			for j in range(self.tamanho): 	
				if self.matriz[i][j].verificada == "S":
					print("verificada")
					lista.append({"linha": i, "coluna":j})
		
		print(lista)
		return lista
		##valores = [ [ j for j in range(self.tamanho) ] for i in range(self.tamanho) if self.matriz[0][0].verificada == "S" ]			
		
		
	def verificarJogada(self, i, j):
		if self.tamanho < i+1:
			raise Exception("Tamanho máximo para (i) excedido. Máximo:" + str(self.tamanho-1))
			
		if self.tamanho < j+1:
			raise Exception("Tamanho máximo para (j) excedido. Máximo: " + str(self.tamanho-1))
		
		self.matriz[i][j].verificada = "S" ## marca posição como verificada
		
		if self.matriz[i][j].conteudo == "B":		
			print("")
			print("!!!!!!!!!!!!!!!!!!!!!!!!")
			print("!!!!!!!!Booooom!!!!!!!!!")
			print("!!!!!!!!!!!!!!!!!!!!!!!!")
			print("")
		else:
			print("")
			print("~~~~~~~~~~~~~~~~~~~~~~~~")
			print("~~~~~~~~~~Água~~~~~~~~~~")
			print("~~~~~~~~~~~~~~~~~~~~~~~~")
			print("")