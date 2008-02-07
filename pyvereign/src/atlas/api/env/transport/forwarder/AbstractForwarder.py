from atlas.api.env.transport.forwarder.Forwarder import Forwarder
from atlas.api.exception.TransportError import TransportError
import socket

class AbstractForwader(Forwarder):
    
    def initialize(self):
        self._inetAddress = None
        self._socket = None
        self._opened = False
        self._protocol = False
    
    def getInetAddress(self):
        return self._inetAddress
    
    def close(self):
        try:
            if not self._socket:
                self._socket.close()
            return True
        except:
            raise
    
    def supportBroadcasting(self, flag):
        raise TransportError("Broadcasting is not supported.")
    
    def isSupportingBroadcasting(self):
        return False
    
    def send(self, stream):
        if not stream:
            raise RuntimeError("Invalid parameter.")
        if not isinstance(stream, str):
            raise TypeError("stream parameter is not an instance of str class.")
    
    def getProtocol(self):
        return self._protocol