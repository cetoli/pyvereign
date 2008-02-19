from atlas.api.env.transport.receiver.Receiver import Receiver
from atlas.api.exception.TransportError import TransportError
import socket

class AbstractReceiver(Receiver):
    
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
            return True
        except:
            raise
        
    def reuseAddress(self, flag):
        if not self._opened:
            raise TransportError("Receiver is not opened.")
        if flag == None:
            raise RuntimeError("flag parameter is none.")
        if not isinstance(flag, bool):
            raise TypeError("flag parameter is not an instance of bool class.")
        if flag:
            self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        else:
            self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 0)
        return self._socket.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR) == 1
    
    def isReusingAddress(self):
        return self._socket.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR) == 1
    
    def receive(self, bufferSize = 1024):
        if bufferSize == None:
            raise RuntimeError("bufferSize parameter is not none.")
        if bufferSize < 1:
            raise RuntimeError("Invalid value for bufferSize parameter.")
        if not isinstance(bufferSize, int):
            raise TypeError("bufferSize parameter is not an instance of int class.")
        
    def getProtocol(self):
        return self._protocol