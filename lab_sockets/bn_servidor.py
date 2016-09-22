import socket
import tabuleiro

ENCODE = "UTF-8"
HOST = '127.0.0.1'   # Endereco IP do Servidor
PORT = 5000          # Porta que o Servidor esta
MAX_BYTES = 65535    # Quantidade de Bytes a serem ser recebidos


def iniciar():
	 #Abrindo um socket UDP na porta 5000
    orig = (HOST, PORT)																
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(orig)

    while True:
        #recebi dados
        data, address = sock.recvfrom(MAX_BYTES) # Recebi dados do socket
        text = data.decode(ENCODE) # Convertendo dados de BASE64 para UTF-8				
        print(address, text)

        if text.startswith("configurar::"):
            configurar(extrairParametro(text))

        #Envia resposta
        text = "Your data was " + str(len(data)) + " bytes long"
        data = text.encode(ENCODE) # Codifica para BASE64 os dados 
        sock.sendto(data, address) # Enviando dados	

    #Fechando Socket
    sock.close()

def configurar(tamanho):
    print("configurar")
    tabuleiro = tabuleiro.Tabuleiro(tamanho)
	
def extrairParametro(comando):
    params = comando.split('::')
    params = params[1]
    print(params)
    return params


iniciar()