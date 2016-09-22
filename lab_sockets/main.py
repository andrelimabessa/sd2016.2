import sys
from udp_server import server
from udp_cliente import client

print("Voce quer executar:")
print("1 para servidor")
print("2 para cliente")
opcao = input("Opcao:")

try:
    if int(opcao) == 1:
        print("Servidor ativado:\n")
        server()
    elif int(opcao) == 2:
        print("Cliente ativado:\n")
        client()

except :
    for val in sys.exc_info():
        print(val)

input()
