from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer


class Bora(object):

    __instance = None

    @staticmethod
    def getInstance():
        if Bora.__instance is None:
            Bora.__instance = Bora()
        return Bora.__instance
    
    def __init__(self):
        self.x = 0    

    def retornaX(self):
        if self.x == None:
            self.x = 0
        else:
            self.x = self.x + 1
        print(str(self.x))

def printName(nome, sobrenome):
    teste = Bora().getInstance()
    teste.retornaX()
    return nome + " " + sobrenome

def server():
    serverRPC = SimpleJSONRPCServer(('localhost', 7002))
    serverRPC.register_function(printName)
    print("Starting server")
    serverRPC.serve_forever()
