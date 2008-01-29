from atlas.api.env.transport.communicationapi.AbstractInetAddress import AbstractInetAddress
import socket

class IPv4Address(AbstractInetAddress):
    
    def __init__(self, ipAddress, port):
        self.initialize()
        self._family = socket.AF_INET
        self._ipAddress = ipAddress
        self._port = port
        