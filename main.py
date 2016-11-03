from BatalhaNaval import BatalhaNaval
import base64
# jogo = BatalhaNaval(5,5)
# jogo.insere_navio(1,1)
# jogo.insere_navio(4,1)
# jogo.insere_navio(2,3)
# jogo.destroi_navio(2,3)

jogo = BatalhaNaval.carregar_jogo()

def mostra_menu():
	print("---------- BATALHA NAVAL ----------")
	print("'0' para sair\n")
	print("'1' para inserir navio\n")
	print("'2' para destruir navio\n")
	print("'3' para exibir o tabuleiro\n")
	print("'4' para salvar o jogo\n")

def executa_comando(comando):
	if comando == 0:
		return 0
	elif comando == 1:
		x = int(input('Insira a posição X para inserir navio: '))
		y = int(input('Insira a posição y para inserir navio: '))
		print(jogo.insere_navio(x, y))
		return 1
	elif comando == 2:
		x = int(input('Insira a posição X para destruir navio: '))
		y = int(input('Insira a posição y para destruir navio: '))
		print(jogo.destroi_navio(x, y))
		return 2
	elif comando == 3:
		print(jogo.exibe_tabuleiro_simples())
		return 3
	elif comando == 4:
		print(jogo.salvar())
		return 4

def inicia_jogo():
	jogando = 1
	while jogando != 0:
		mostra_menu()		
		comando = input('Insira um comando: ')
		jogando = executa_comando(int(comando))

	print("FIM DO JOGO")
		
inicia_jogo()
# jogo.salvar()
# string = "b'eydOQVVGUkFHSU8nOiAnWCcsICdNQVhfSk9HQURBUyc6IC00LCAnQUdVQSc6IDAsICdOQVZJTyc6IDEsICd0YWJ1bGVpcm8nOiBbWzAsIDAsIDAsIDAsIDBdLCBbMCwgMSwgMCwgMCwgMF0sIFswLCAwLCAwLCAnWCcsIDBdLCBbMCwgMCwgMCwgMCwgMF0sIFswLCAxLCAwLCAwLCAwXV19'"

# a = string[2:-1] #base64.b64encode(bytes(string, "utf-8"))
# b = base64.b64decode(a)

# print(b)