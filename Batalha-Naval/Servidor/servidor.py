import socket
import sys
import BatalhaNaval
import udp_server
from datetime import datetime


a = BatalhaNaval.BatalhaNaval(3)
def iniciar():
    a = BatalhaNaval.BatalhaNaval(3)


def action(opcao):
    try:
      #  if int(opcao) == 1:
       #     return iniciar()
        #elif int(opcao) == 2:
      if a.numMaximoJogadas == 0:
          return "0"
      else:
          xy = opcao.split("-")
          print(xy[0])
          print(xy[1])
          return a.jogada(int(xy[0]), int(xy[1]))

    except:  # pega todas possíveis
        for val in sys.exc_info():
            print(val)




