import socket

ENCODE = "UTF-8"
HOST = '127.0.0.1'   # Endereco IP do Servidor
PORT = 5000          # Porta que o Servidor esta
MAX_BYTES = 65535    # Quantidade de Bytes a serem ser recebidos

def client(text):
    data = text.encode(ENCODE)  # Codifica para BASE64 os dados de entrada
    # Enviod de dados
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Inicializar um socket UDP
    dest = (HOST, PORT)  # Define IP de origem e Porta de destino
    sock.sendto(data, dest)  # Envia os dados para o destino

    data, address = sock.recvfrom(MAX_BYTES)  # Recebi dados do socket
    text = data.decode(ENCODE)  # Convertendo dados de BASE64 para UTF-8
    print (text)
    return text

    # Fechando Socket
    sock.close()

def receber(self):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Inicializar um socket UDP
    dest = (HOST, PORT)  # Define IP de origem e Porta de destino

    while True:
        # recebi dados
        data, address = sock.recvfrom(MAX_BYTES)  # Recebi dados do socket
        text = data.decode(ENCODE)  # Convertendo dados de BASE64 para UTF-8
        # Fechando Socket
        sock.close()
        return text, address

