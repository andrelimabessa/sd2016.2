import zmq
import sys
import random

from datetime import datetime

ENCODE = "UTF-8"
HOST = '127.0.0.1'   # Endereco IP do Servidor
PORT = 5000          # Porta que o Servidor esta
MAX_BYTES = 65535    # Quantidade de Bytes a serem ser recebidos

global nome

def client():

    identificado = False

    while identificado == False:        
        nick = input("Nome do jogador: ")
        cmd = "nw:" + nick
        if comunicar(cmd):
            identificado = True
            print("Olá " + nick + "! Você foi registrado no servidor. Pronto para jogar.")

    while True:
        """ Procedimento responsável por enviar dados para o servidor e receber alguma resposta por conta disso """                

        print("\nComandos disponíveis:")        
        print("     1. Atirar")        
        print("     0. Sair")        
        print("----------------------------------------------------\n")
        text = input("Digite o comando: ")   		    # Recebe dados

        if text == "0":
            return
        elif text == "1":
            text = requisicaoAtirar(nick)
            comunicar(text)
        else:        
            print("\nComando desconhecido\n")

def comunicar(text):

    # trecho extráido do queue_client
    port = "5559"
    context = zmq.Context()
    print ("Conectando com o servidor...")
    socket = context.socket(zmq.REQ)
    socket.connect ("tcp://localhost:%s" % port)
    #client_id = random.randrange(1,10005)

    data = text.encode("UTF-8")
    socket.send (data)
    #  Pega a resposta.
    message = socket.recv()
    retorno = message.decode("UTF-8")
    #print("Resposta recebida [", retorno, "]")

    return verificarSucesso(retorno)

def requisicaoAtirar(nick):
    cmd = ""     
    i = input("Posicao I (0 a 4) :")
    j = input("Posicao J (0 a 4) :")        
    cmd = "fi:" + nick + ":" + i + "-" + j

    return cmd

def verificarSucesso(text): 
    if len(text) > 4:
        retorno = text[0:4]
        codigo = text[4:7]
        if retorno == "ERR:":            
            print("**ERRO:" + getMensagemErro(codigo) + "**")

            return False
        elif retorno == "COD:":            
            print(getMensagemSucesso(codigo))
            return True    

        return False

    return True

def getMensagemErro(codigo):    
    if codigo == "100":
        return "Nick já utilizado"

def getMensagemSucesso(codigo):    
    if codigo == "200":        
        return "\n!!!!!!!!!!!!!!!!!!!!!!!!\n!!!!!!  Booooom  !!!!!!!\n!!!!!!!!!!!!!!!!!!!!!!!!\n"
    if codigo == "201":
        return "\n~~~~~~~~~~~~~~~~~~~~~~~~\n~~~~~~~   Água   ~~~~~~~\n~~~~~~~~~~~~~~~~~~~~~~~~\n"
    if codigo == "202":
        return "** Posição além do tamanho do tabuleiro **"        
    if codigo == "203":
        return "----- Sem jogada restante ------\n ----- Voce perdeu ------"
    if codigo == "204":
        return "----- Posição já verificada ------"


