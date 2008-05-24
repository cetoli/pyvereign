from org.pyvereign.core.environment.transport.forwarder.AbstractForwarder import AbstractForwader
from org.pyvereign.core.environment.transport.address.InetAddress import InetAddress
from org.pyvereign.core.exception.TransportError import TransportError
from org.pyvereign.core.environment.instrumentation.dto.networking.NetworkProtocol import NetworkProtocol
import socket

class StreamForwarder(AbstractForwader):
    """
    Defines the forwarder implementation over TCP protocol.
    
    @author: Fabricio
    @since: 
    @version: 0.0.1
    """
    
    def __init__(self, inetAddress, protocol):
        """
        Initializes the StreamForwarder object.
        
        @param inetAddress: a InetAddress object.
        @type inetAddress: L{InetAddress}
        @param protocol: a NetworkProtocol object.
        @type protocol: L{NetworkProtocol}
        @return: None
        """
        if not inetAddress:
            raise RuntimeError("inetAddress parameter is none.")
        if not isinstance(inetAddress, InetAddress):
            raise TypeError("inetAddress parameter is not instance of InetAddress class.")
        if inetAddress.isBroadcastAddress():
            raise TransportError("Stream forwarder not support broadcasting.")
        if not protocol:
            raise RuntimeError("protocol parameter is none.")
        if not isinstance(protocol, NetworkProtocol):
            raise TypeError("protocol parameter is not an instance of Protocol class.")
        self.init(inetAddress, None, False, protocol)
        
    def open(self):
        try:
            self._socket = socket.socket(self._inetAddress.getFamily(), socket.SOCK_STREAM)
            self._opened = True
            return self._opened
        except socket.error, e:
            raise TransportError(e)
    
    def send(self, stream):
        AbstractForwader.send(self, stream)
        if not self._opened:
            raise TransportError("Stream forwarder is not opened.")
        try:
            if self._inetAddress.isBindAddress():
                self._socket.connect((self._inetAddress.getIPAddress(), self._inetAddress.getPort()))
            else:
                self._socket.connect(self._inetAddress.getTuple())
            self._socket.send(stream)
            return stream
        except socket.error, e:
            raise TransportError(e)