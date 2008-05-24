from org.pyvereign.core.environment.transport.receiver.Receiver import Receiver
from org.pyvereign.core.exception.TransportError import TransportError
import socket

class AbstractReceiver(Receiver):
    """
    Defines some common implementations for Receiver objects.
    
    @author: Fabricio
    @since: 
    @version:  
    """
    
    def init(self, inetAddress, socket, opened, protocol):
        """
        Defines initialization parameters.
        
        @param inetAddress: an InetAddress object
        @type inetAddress: L{InetAddress}
        @param socket: a socket object
        @type socket: socket
        @param opened: a flag to determinate if the receiver object is opened.
        @type opened: bool
        @param protocol: the network protocol of receiver.
        @type protocol: L{NetworkProtocol}
        """
        self._inetAddress = inetAddress
        """
        @ivar: the destination address.
        @type: L{InetAddress}  
        """
        self._socket = socket
        """
        @ivar: a socket object
        @type: socket  
        """
        self._opened = opened
        """
        @ivar: a flag to determinate if the forwarder object is opened.
        @type: bool  
        """
        self._protocol = protocol
        """
        @ivar: the network protocol of forwarder.
        @type: L{NetworkProtocol} 
        """
    
    def getInetAddress(self):
        return self._inetAddress
    
    def close(self):
        try:
            if not self._socket:
                self._socket.close()
                del self._socket
            return True
        except socket.error, e:
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