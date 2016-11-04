import sys
from udp_server import server
from udp_cliente import client

print("Você quer jogar?")
print("1 Irá Iniciar o Servidor")
print("2 Irá Iniciar o Jogo")
opcao = input("Opção:")

try:
    if int(opcao) == 1:
        server()
    elif int(opcao) == 2:
        print("Jogo startado:\n")
        client()

except : # pega todas possíveis
    for val in sys.exc_info():
        print(val)

input()
