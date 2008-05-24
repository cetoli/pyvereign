from org.pyvereign.core.environment.transport.forwarder.Forwarder import Forwarder
from org.pyvereign.core.exception.TransportError import TransportError

class AbstractForwader(Forwarder):
    """
    Defines some common implementation for Forwarder objects.
    
    @author: Fabricio
    @since: 
    @version: 0.0.1
    """
    
    def init(self, inetAddress, socket, opened, protocol):
        """
        Defines initilization parameters of Forwarder objects.
        
        @param inetAddress: the destination address.
        @type inetAddress: L{InetAddress}
        @param socket: a socket object
        @type socket: socket
        @param opened: a flag to determinate if the forwarder object is opened.
        @type opened: bool
        @param protocol: the network protocol of forwarder.
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