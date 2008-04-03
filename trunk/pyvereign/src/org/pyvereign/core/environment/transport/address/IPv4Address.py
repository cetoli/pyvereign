from org.pyvereign.core.environment.transport.address.AbstractInetAddress import AbstractInetAddress
import socket

class IPv4Address(AbstractInetAddress):
    
    def __init__(self, ipAddress, port):
        self.initialize()
        self._family = socket.AF_INET
        self._ipAddress = ipAddress
        self._port = port
    
    def isBroadcastAddress(self):
        return False
    
    def isBindAddress(self):
        return False
        