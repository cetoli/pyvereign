from org.pyvereign.core.environment.transport.address.IPv4Address import IPv4Address

class BindIPv4Address(IPv4Address):
    """
    Defines the impletation of bind address for IPv4Address.
    @author: Fabricio
    @since: 
    @version: 0.0.1
    """
    
    def __init__(self, port = 5050):
        IPv4Address.__init__(self, '127.0.0.1', port)
        
    def getIPAddress(self):
        return "127.0.0.1"
        
    def isBindAddress(self):
        return True
    
    def getTuple(self):
        return ('', self._port)