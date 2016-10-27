import rpyc

def resposta(string):
    print(repr(string))

def client():
    
    config = {'allow_public_attrs': True}
    proxy = rpyc.connect('localhost', 18861, config=config)

    fileobj = open('testfile.txt')
    linecount = proxy.root.line_counter(fileobj, resposta)
    print('O número de linhas no arquivo é:', linecount)

    nome = linecount = proxy.root.print_name("André", "Bessa")
    print(nome)
