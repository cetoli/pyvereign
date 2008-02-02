from atlas.api.env.transport.address.InetAddress import InetAddress

class AbstractInetAddress(InetAddress):
    
    def initialize(self):
        self._family = None
        self._ipAddress = ""
        self._port = 0
        
    def getFamily(self):
        return self._family
    
    def getIPAddress(self):
        return self._ipAddress
    
    def getPort(self):
        return self._port
    
    def getTuple(self):
        return (self._ipAddress, self._port)