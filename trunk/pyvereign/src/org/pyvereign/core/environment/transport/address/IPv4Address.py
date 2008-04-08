from org.pyvereign.core.environment.transport.address.AbstractInetAddress import AbstractInetAddress
import socket

class IPv4Address(AbstractInetAddress):
    """
    Defines the implementation of IPv4Address.
    
    @author: Fabricio
    @since: 
    @version: 0.0.1
    """
    
    def __init__(self, ipAddress, port):
        """
        Initializes IPv4Address objects.
        @param ipAddress: the ip address of IPv4Addresss.
        @type ipAddress: str
        @param port: the port of IPv4Address
        @type port: int
        @rtype: L{IPv4Address} 
        """
        self.init()
        self._family = socket.AF_INET
        self._ipAddress = ipAddress
        self._port = port
    
    def isBroadcastAddress(self):
        return False
    
    def isBindAddress(self):
        return False
        