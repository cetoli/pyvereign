from org.pyvereign.core.environment.transport.address.InetAddress import InetAddress

class AbstractInetAddress(InetAddress):
    """
    Defines the common implementation of InetAddress interface.
    
    @author: Fabrício
    @since: 
    @version: 0.0.1
    """
    
    def init(self):
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
    
    def setPort(self, port):
        self._port = port