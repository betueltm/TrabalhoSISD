#!flask/bin/python
import sys
import time
from flask import Flask
from flask import request
import Pyro4
import Pyro4.util
from serveraplicacao import ServerAplicacao
from server import Server
import threading

sys.excepthook = Pyro4.util.excepthook

servers = []
uri_servidores = ['PYRO:obj_c9e1fe08fb2942238f101f272c50638f@localhost:53358','PYRO:obj_0ba696c2ac1c4f06a162e89835624a50@localhost:53354','PYRO:obj_8e7180d711144211bed819a0784bc9e0@localhost:53352']

def preencheServers():
    global servers
    while(True):
        servers = []
        for i in range(3):
            server = Pyro4.Proxy("PYROURI:" + uri_servidores[i])
            novo_servidor = server.dados_servidor()        
            novo_servidor.nome = i + 1
            novo_servidor.uri = uri_servidores[i]
            servers.append(novo_servidor)
        servers.sort(key = lambda x: x.cpu)
        time.sleep(20)
        

app = Flask(__name__)

@app.route('/produto', methods=['POST'])
def post():
    content = request.get_json()
    produto = str(content['nome'])
    server = Pyro4.Proxy("PYROURI:" + servers[0].uri)
    server.cadastrar(produto)

    return 'JSON posted'

@app.route('/gettoken', methods=['GET'])
def get():
    return 'token para ' + request.args.get('nome')

threading.Thread(name='atualiza_servidores',target=preencheServers,daemon=True).start()
app.run()

