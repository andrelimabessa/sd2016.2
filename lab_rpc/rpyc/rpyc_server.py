import rpyc

class MyService(rpyc.Service):

    def exposed_line_counter(self, fileobj, function):
        print('Cliente chamou line counter')
        for linenum, line in enumerate(fileobj.readlines()):
            function(line)
        return linenum + 1

    def exposed_print_name(self, nome, sobrenome):
        return nome + " " + sobrenome

def server():
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyService, port = 18861)
    t.start()
