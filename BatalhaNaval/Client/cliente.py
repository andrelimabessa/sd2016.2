import sys

import udp_cliente


def menu():
    trailMessage = ""
    try:

        while trailMessage != "0":
            x = int(input("Insira a coordenada do eixo X: "))
            y = int(input("Insira a coordenada do eixo Y: "))
            trailMessage = (udp_cliente.client(str(x)+"-"+str(y)))

    except :
        for val in sys.exc_info():
            print(val)