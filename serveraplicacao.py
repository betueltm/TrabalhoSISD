from __future__ import print_function
import Pyro4
from server import Server
import os
import psutil

@Pyro4.expose
@Pyro4.behavior(instance_mode="single")

class ServerAplicacao(object):
    #def __init__(self):
        
    def cadastrar(self,produto):
        return True
    
    def dados_servidor(self):
        servidor = Server('','',psutil.cpu_percent(),psutil.virtual_memory()[2])
        
        return servidor       

def main():
    Pyro4.Daemon.serveSimple(
        {
            ServerAplicacao: "example.ServerAplicacao"
        },
        ns = True)

if __name__ == "__main__":
    main()