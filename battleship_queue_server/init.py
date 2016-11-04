import sys
import imp

from inicializador import Inicializador

if len(sys.argv) > 1:
    argv = sys.argv[1]

    print('Opções: client, server, queue_server')
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
    elif argv == 'queue_server':
        try:
            Inicializador.queue_server()
        except:
            pass
    else:
        print('Opção inválida!')
