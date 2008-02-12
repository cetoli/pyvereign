from atlas.api.env.transport.forwarder.Forwarder import Forwarder
from atlas.api.exception.TransportError import TransportError
import socket

class AbstractForwader(Forwarder):
    
    def initialize(self):
        self._inetAddress = None
        self._socket = None
        self._opened = False
        self._protocol = None
    
    def getInetAddress(self):
        return self._inetAddress
    
    def close(self):
        try:
            if not self._socket:
                self._socket.close()
            self._opened = False
            return self._opened == False
        except:
            raise
        
    def setTimeout(self, timeout):
        if not self._opened:
            raise TransportError("Forwarder is not opened.")
        if timeout == None:
            raise RuntimeError("timeout parameter is none")
        if not isinstance(timeout, int):
            raise TypeError("timeout parameter is not an instance of int class.")
        if timeout < 1:
            raise RuntimeError("Negative timeout.")
        self._socket.settimeout(timeout)
        return self._socket.gettimeout()
    
    def getTimeout(self):
        if not self._opened:
            raise TransportError("Forwarder is not opened.")
        return self._socket.gettimeout()
    
    def supportBroadcasting(self, flag):
        raise TransportError("Broadcasting is not supported.")
    
    def isSupportingBroadcasting(self):
        return False
    
    def hasSupportToBroadcasting(self):
        return False
    
    def send(self, stream):
        if not stream:
            raise RuntimeError("Invalid parameter.")
        if not isinstance(stream, str):
            raise TypeError("stream parameter is not an instance of str class.")
    
    def getProtocol(self):
        return self._protocol