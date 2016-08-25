import BatalhaNaval

a = BatalhaNaval.BatalhaNaval(3)
a.initBarcos()
while a.numeroDeJogadas > 0:
	a.jogada()
	print("Jogadas disponiveis: " + str(a.numeroDeJogadas))
print("Acabaram as jogadas")
# a.limpaLog("LogDeJogadas.txt")
# a.limpaLog("LogDoTabuleiro.txt")
# a.limpaLog("LogNumeroDeJogadas.txt")