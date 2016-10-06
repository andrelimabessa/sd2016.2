import sys
from udp_server import server
from udp_cliente import client
from udp_server_thread import server_thread_procedural
from udp_server_thread import server_thread_oo


print("Você quer executar:")
print("1 para servidor simples")
print("2 para servidor thread")
print("3 para cliente")
opcao = input("Opção:")


try:
    if int(opcao) == 1:
        print("Servidor ativado:\n")
        server()
    elif int(opcao) == 2:
        print("Servidor com thread ativado:\n")
        server_thread_procedural()
    elif int(opcao) == 3:
        print("Cliente ativado:\n")
        client()

except :
    for val in sys.exc_info():
        print(val)

input()
