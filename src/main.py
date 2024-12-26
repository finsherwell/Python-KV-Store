from gevent import socket
from gevent.pool import Pool
from gevent.server import StreamServer

from collections import namedtuple
from socket import error as socket_error
from dotenv import load_dotenv, set_key

from config import determine_persistence_path
from protocols import ProtocolHandler

Error = namedtuple('Error', ('message',))

class Server:
    def __init__(self, host='127.0.0.1', port=31337, max_clients=64):
        self._pool = Pool(max_clients)
        self._server = StreamServer(
            (host, port),
            self.connection_handler,
            spawn=self._pool)
        self._protocol = ProtocolHandler()
        self._kv = {}
    
    def run(self):
        self._server.serve_forever()

class Client:
    def __init__(self):
        def __init__(self, host='127.0.0.1', port=31337):
            self._protocol = ProtocolHandler()
            self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._socket.connect((host, port))

if __name__ == "__main__":
    from gevent import monkey; monkey.patch_all()
    set_key(".env", "DATA_LOGGING_FILE", determine_persistence_path('kv-logging'))
    set_key(".env", "DATA_SNAPSHOT_FILE", determine_persistence_path('kv-snapshots'))
    Server().run()