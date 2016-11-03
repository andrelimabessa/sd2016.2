import sys
import imp

from inicializador import Inicializador

if len(sys.argv) > 1:
    argv = sys.argv[1]

    if argv == 'client':
        try:
            Inicializador.client()
        except:
            pass

    elif argv == 'server':
        try:
            Inicializador.server()
        except:
            pass
