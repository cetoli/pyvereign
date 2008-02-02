from atlas.api.env.transport.socket_adapter.SocketAdapter import SocketAdapter

class AbstractSocketAdapter(SocketAdapter):
    
    def initialize(self):
        self._socket = None
        self._inetAddress = None
    
    def getInetAddress(self):
        return self._inetAddress
    
    def open(self):
        pass
    
    def close(self):
        if not self._socket:
            self._socket.close()
        
        