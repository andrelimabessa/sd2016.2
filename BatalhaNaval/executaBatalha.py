import BatalhaNaval

a = BatalhaNaval.BatalhaNaval(3)
# a.initBarcos()
while a.numeroDeJogadas > 0:
	a.jogada()
print("Acabaram as jogadas")
#Metodo sendo usado assim para facilitar testes.
# TODO corrigir metodo
a.limpaLog("LogDeAcertos.txt")
a.limpaLog("LogDoTabuleiro.txt")
a.limpaLog("LogNumeroDeJogadas.txt")
a.limpaLog("LogPosicaoBarcos.txt")