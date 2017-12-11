from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

import logging
import time
import datetime
import json

from flask import Flask
from flask_sockets import Sockets

app = Flask(__name__)
sockets = Sockets(app)

logging.basicConfig()
rpc_user = "alice"
rpc_password = "helloworldonlylocal"

# rpc_user and rpc_password are set in the bitcoin.conf file
rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:8332"%(rpc_user, rpc_password))
r = rpc_connection

def lastBlockHash(): return r.getbestblockhash()

def lastBlockHeight():
    best = r.getbestblockhash()
    block = r.getblock(best)
    return block['height']

def durationSinceLastBlock():
    best = r.getbestblockhash()
    block = r.getblock(best)
    return int(time.time()) - block['time']

def transactionsLastBlock():
    best = r.getbestblockhash()
    block = r.getblock(best)
    return len(block['tx'])

def transactionsNextBlock():
    nextblock = r.getblocktemplate()
    transactions = nextblock['transactions']
    return len(transactions)

def myInfo():
    return {
         'lastBlockHeight': lastBlockHeight(),\
         'lastBlockHash': lastBlockHash(),\
         'transactionsLastBlock': transactionsLastBlock(),\
         'transactionsNextBlock': transactionsNextBlock(),\
         'secondsSinceLastBlock': durationSinceLastBlock()}

@sockets.route('/bitcoin')
def echo_socket(ws):
    while not ws.closed:
        ws.send(json.dumps(myInfo()))
	time.sleep(1)

@app.route('/')
def hello():
    return 'Bitcoin WS info'

if __name__ == "__main__":
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    server = pywsgi.WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
    server.serve_forever()
