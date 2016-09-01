import base64
import random
class BatalhaNaval(object):

	AGUA = 0
	NAVIO = 1
	NAUFRAGIO = 'X'
	MAX_JOGADAS = 10
	NOME_DO_ARQUIVO = 'jogo_batalha_naval.txt'

	# def __init__(self, w, h):
	# 	self.tabuleiro = [[self.AGUA for x in range(w)] for y in range(h)] 

	def insere_navio(self, x, y):
			self.tabuleiro[x][y] = self.NAVIO
			self.MAX_JOGADAS -= 1

	def destroi_navio(self, x, y):
		if self.MAX_JOGADAS > 0:
			if self.tabuleiro[x][y] == self.NAVIO:
				self.tabuleiro[x][y] = self.NAUFRAGIO
				print("---------------------------------------------------------\n\n")
				print("^.................. Navio naufragado ..................^")
				print("\n\n---------------------------------------------------------")
			else:
				print("---------------------------------------------------------\n\n")
				print("^.................. Errrrôôôooo ..................^")
				print("\n\n---------------------------------------------------------")
			self.MAX_JOGADAS -= 1
		else:
			print("JOGADAS EXCEDIDAS")

	def exibe_tabuleiro(self):
		for i in range(len(self.tabuleiro)):
			linha = "|"
			for j in range(len(self.tabuleiro[i])):
				if self.tabuleiro[i][j] == self.AGUA:
					linha = linha + " " + "AGUA" + " |"
				elif self.tabuleiro[i][j] == self.NAVIO:
					linha = linha + " " + "NAVIO" + " |"
				elif self.tabuleiro[i][j] == self.NAUFRAGIO:
					linha = linha + " " + "NAUFRAGIO" + " |"
			print(linha)

	def exibe_tabuleiro_simples(self):
		for i in range(len(self.tabuleiro)):
			print(self.tabuleiro[i])

	def salva_estado_do_jogo(self):
		print("Salvando")

	def to_json(self):
		json = {
			'AGUA': self.AGUA,
			'NAVIO': self.NAVIO,
			'NAUFRAGIO': self.NAUFRAGIO,
			'MAX_JOGADAS': self.MAX_JOGADAS,
			'tabuleiro': self.tabuleiro
		}
		return json

	def salvar(self):
		json_string = str(self.to_json())
		self.escreve_arquivo(json_string)

	def escreve_arquivo(self, string):
		arquivo = open(BatalhaNaval.NOME_DO_ARQUIVO,'w+')
		arquivo.write(str(self.criptografa(string))) 
		arquivo.close()
	
	def criptografa(self, string):
		return base64.b64encode(bytes(string, "utf-8"))

	@staticmethod
	def json_to_object(json):
		classe = BatalhaNaval()
		classe.AGUA = json.get('AGUA')
		classe.NAVIO = json.get('NAVIO')
		classe.NAUFRAGIO = json.get('NAUFRAGIO')
		classe.MAX_JOGADAS = json.get('MAX_JOGADAS')
		classe.tabuleiro = json.get('tabuleiro')
		return classe

	@staticmethod
	def carregar_jogo():
		string = BatalhaNaval.ler_arquivo()
		json = eval(string)
		return BatalhaNaval.json_to_object(json)

	@staticmethod
	def ler_arquivo():
		arquivo = open(BatalhaNaval.NOME_DO_ARQUIVO,'r')
		string = arquivo.read()
		arquivo.close()
		if len(string) > 0:
			return BatalhaNaval.descriptografa(string)
		else:
			jogo = BatalhaNaval.json_to_object(eval("{'NAUFRAGIO': 'X', 'MAX_JOGADAS': 10, 'AGUA': 0, 'NAVIO': 1, 'tabuleiro': []}"))
			jogo.tabuleiro = BatalhaNaval.gera_tabuleiro_randomico()
			return str(jogo.to_json())

	@staticmethod
	def gera_tabuleiro_randomico():
		tabuleiro = [[0 for x in range(10)] for y in range(10)] 
		for i in range(50):
			x = random.randint(0, 9)
			y = random.randint(0, 9)
			tabuleiro[x][y] = 1
		return tabuleiro

	@staticmethod
	def descriptografa(string):
		str_hash = string[2:-1]
		return base64.b64decode(str_hash).decode("utf-8", "ignore")