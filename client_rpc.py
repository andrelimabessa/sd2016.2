#coding: utf-8
import rpyc

config = {'allow_public_attrs': True}
proxy = rpyc.connect('localhost', 18861, config=config)

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
        print(x, y)
        data = str({"comando": 1, "x": x, "y": y})
        print(proxy.root.tratar(data))
    elif comando == 2:
        x = int(input('Insira a posição X para destruir navio: '))
        y = int(input('Insira a posição y para destruir navio: '))
        print(x, y)
        data = str({"comando": 2, "x": x, "y": y})
        print(proxy.root.tratar(data))
    elif comando == 3:
        data = str({"comando": 3})
        print(proxy.root.tratar(data))
    elif comando == 4:
        data = str({"comando": 4})
        print(proxy.root.tratar(data))

def inicia_jogo():
    jogando = 1
    while jogando != 0:
        mostra_menu()       
        comando = input('Insira um comando: ')
        jogando = executa_comando(int(comando))

    print("FIM DO JOGO")
 
inicia_jogo()



# proxy.root.line_counter(fileobj, resposta)