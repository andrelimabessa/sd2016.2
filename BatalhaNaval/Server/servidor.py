import sys

import BatalhaNaval

a = BatalhaNaval.BatalhaNaval(3)
def iniciar():
    a = BatalhaNaval.BatalhaNaval(3)


def action(option):
    try:
      if a.numeroDeJogadas == 0:
          return "0"
      else:
          xy = option.split("-")
          print(xy[0])
          print(xy[1])
          return a.jogada(int(xy[0]), int(xy[1]))

    except:
        for val in sys.exc_info():
            print(val)