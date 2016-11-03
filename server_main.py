import socket
HOST = ''              # Endereco IP do Servidor
PORT = 5555            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
while True:
    con, cliente = tcp.accept()
    print('Concetado por' + " " + str(cliente))
    while True:
        msg = con.recv(1024)
        if not msg: break
        print(cliente + " " + str(msg))
    print('Finalizando conexao do cliente' + " " + str(cliente))
    con.close()
