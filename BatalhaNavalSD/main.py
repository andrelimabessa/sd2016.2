import sys
from udp_server import server
from udp_cliente import client

print("Você quer jogar?")
print("1 para iniciar servidor")
print("2 para iniciar jogo")
opcao = input("Opção:")

try:
    if int(opcao) == 1:
        server()
    elif int(opcao) == 2:
        print("Jogo Iniciado:\n")
        client()

except : # pega todas possíveis
    for val in sys.exc_info():
        print(val)

input()
