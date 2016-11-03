#coding: utf-8
import rpyc
from BatalhaNaval import BatalhaNaval

jogo = BatalhaNaval.carregar_jogo()

class MyService(rpyc.Service):

    def exposed_tratar(self, data):
        dictData = eval(data)
        comando = dictData.get('comando')
        resposta = ""

        if comando == 0:
            resposta = "voce saiu"
        elif comando == 1:
            x = dictData.get('x')
            y = dictData.get('y')
            resposta = jogo.insere_navio(x, y)
        elif comando == 2:
            x = dictData.get('x')
            y = dictData.get('y')
            resposta = jogo.destroi_navio(x, y)
        elif comando == 3:
            resposta = jogo.exibe_tabuleiro_simples()
        elif comando == 4:
            jogo.salvar()
            resposta = "jogo salvo"

        print(resposta)
        return resposta

def server():
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyService, port = 18861)
    t.start()

server()