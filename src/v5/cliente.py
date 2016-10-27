from jsonrpclib import Server

global nick

def client():

    proxy = Server('http://localhost:7002')
    identificado = False

    while identificado == False:            
    #    requisicaoIncluirJogador(proxy)
        nick = input("Nome do jogador: ")
        resultado = proxy.incluirJogador(nick)    
        
        print("resultado: ", resultado)
        if resultado == "sucesso":
            print("Olá " + nick + "! Você foi registrado no servidor. Pronto para jogar.")
            identificado = True        

    while True:
        """ Procedimento responsável por enviar dados para o servidor e receber alguma resposta por conta disso """                

        print("\nComandos disponíveis:")        
        print("     1. Atirar")        
        print("     0. Sair")        
        print("----------------------------------------------------\n")
        text = input("Digite o comando: ")   		    # Recebe dados

        if text == "0":
            return
        elif text == "1":
            requisicaoAtirar(proxy, nick)            
        else:
            print("\nComando desconhecido\n")

def requisicaoIncluirJogador(proxy): 
    nick = input("Nome do jogador: ")
    resultado = proxy.incluirJogador(nick)    
    print("resultado: ", resultado)
    if resultado == "sucesso":
        print("Olá " + nick + "! Você foi registrado no servidor. Pronto para jogar.")

    resultado == "sucesso"


def requisicaoAtirar(proxy, nick):    
    i = input("Posicao I (0 a 4) :")
    j = input("Posicao J (0 a 4) :")

    print(proxy.atirar(nick, i, j))    
