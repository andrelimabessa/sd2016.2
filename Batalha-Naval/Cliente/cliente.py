import sys
from _operator import concat

import udp_cliente
from datetime import datetime


def menu():
    # 0 Inicia o jogo
   # print("1 para fazer jogada")
  #  print("2 para f")
  #  opcao = input("Opção:")
    msn = ""
    try:

        while msn != "0":

            #if int(opcao) == 1:
             #  udp_cliente.client("1")


           # if int(opcao) == 2:
            #print(udp_cliente.client("2"))
            x = int(input("Digite a posicao do eixo X:"))
            y = int(input("Digite a posicao do eixo Y:"))
            msn = (udp_cliente.client(str(x)+"-"+str(y)))

    except : # pega todas possíveis
        for val in sys.exc_info():
            print(val)
