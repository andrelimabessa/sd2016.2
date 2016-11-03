import BatalhaNavalSD
#a = int(input("Informe o numero de colunas: "))
#b = int(input("Informe o numero de linhas: "))

partida = BatalhaNavalSD.batalhaNaval(3)

while partida.numJogadas > 0:
    partida.jogada()

    if partida.numBarcos == 0:
        print("Você destruiu todos os barco,Parabéns!")
        break
    elif partida.numBarcos>0 and partida.numJogadas>0:
        print("Você ainda possui " + str(partida.numJogadas) + " jogada(s).")
    else:
        print("Acabaram suas jogadas!")
partida.limparLogs()
print("Fim de Jogo")