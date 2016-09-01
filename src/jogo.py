import batalhanaval

print("~~~~~~~~~~Bem-vindo ao Jogo~~~~~~~~~~")

## bloco de métodos	
def exibirMenu(partida):

	print("")
	print("-----------------------------")
	if partida.ativa == "N":
		print("1. Iniciar")
	if partida.ativa == "S":
		print("2. Disparar")
		
	print("7. Carregar jogo")
	
	if partida.ativa == "S":
		print("8. Salvar jogo")
		
	print("9. Sair")
	
	if partida.ativa == "S":
		print("")
		print("Jogadas restante: " , partida.jogadaRestante)
	print("-----------------------------")


def iniciarPartida(partida):	
	partida.definirTabuleiro()
		
def disparar(partida):	
	x = input("Informe linha: ")
	y = input("Informe coluna: ")
	
	partida.atirar( int(x),int(y) );
	
def salvar(partida):
	partida.salvarJogo()
	
def carregar(partida):
	iniciarPartida(partida)
	partida.carregarJogo()
	print(partida)

#####################
## bloco principal ##
#####################

partida = batalhanaval.BatalhaNaval(5, 5)

while 1 == 1:		
	exibirMenu(partida)
	menu = input("O que deseja fazer: ")
	
	if menu == "1":
		iniciarPartida(partida)
		
	if menu == "2":
		disparar(partida)
		
	if menu == "7":
		carregar(partida)
	
	if menu == "8":
		salvar(partida)
		
	if menu == "9":
		print("Finalizando jogo.....")
		exit(0)