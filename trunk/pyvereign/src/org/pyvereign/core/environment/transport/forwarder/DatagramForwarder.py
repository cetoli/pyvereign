from org.pyvereign.core.environment.transport.forwarder.AbstractForwarder import AbstractForwader
from org.pyvereign.core.environment.transport.address.InetAddress import InetAddress
from org.pyvereign.core.environment.instrumentation.dto.networking.NetworkProtocol import NetworkProtocol
from org.pyvereign.core.exception.TransportError import TransportError
import socket

class DatagramForwarder(AbstractForwader):
    """
    Defines the forwarder implementation over UDP protocol.
    
    @author: Fabricio
    @since: 
    @version: 0.0.1
    """
    
    def __init__(self, inetAddress, protocol):
        """
        Initializes the DatagramForwarder object.
        
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
        if not protocol:
            raise RuntimeError("protocol parameter is none.")
        if not isinstance(protocol, NetworkProtocol):
            raise TypeError("protocol parameter is not an instance of Protocol class.")
        self.init(inetAddress, None, False, protocol)
    
    def open(self):
        try:
            self._socket = socket.socket(self._inetAddress.getFamily(), socket.SOCK_DGRAM)
            self._opened = True
            return self._opened
        except socket.error, e:
            raise TransportError(e)
    
    def supportBroadcasting(self, flag):
        if not self._opened:
            raise TransportError("Datagram forwarder is not opened.")
        if flag == None:
            raise RuntimeError("Invalid parameter.")
        if not isinstance(flag, bool):
            raise TypeError("flag parameter is not instance of bool class.")
        if flag:
            self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        else:
            self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 0)
        return self._socket.getsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST) == 1
    
    def isSupportingBroadcasting(self):
        return self._socket.getsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST) == 1
    
    def send(self, stream):
        AbstractForwader.send(self, stream)
        if not self._opened:
            raise TransportError("Datagram forwarder is not opened.")
        try:
            self._socket.sendto(stream, (self._inetAddress.getIPAddress(), self._inetAddress.getPort()))
            return stream
        except socket.error, e:
            raise TransportError(e)
    
    def hasSupportToBroadcasting(self):
        return True