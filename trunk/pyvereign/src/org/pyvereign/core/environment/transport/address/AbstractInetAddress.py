from org.pyvereign.core.environment.transport.address.InetAddress import InetAddress

class AbstractInetAddress(InetAddress):
    """
    Defines the common implementation of InetAddress interface.
    
    @author: Fabricio
    @since: 16/01/2008 - 18:00:47 
    @version: 0.0.1
    """
    
    def init(self, family, ipAddress, port):
        """
        Defines initilization parameters of InetAddress objects.
        @param family: the family of InetAddress.
        @type family: int 
        @param ipAddress: the ip address of InetAddress.
        @type ipAddress: str
        @param port: the port of InetAddress.
        @type port: int
        @rtype: None
        """
        self._family = family
        """
        @ivar: the family of InetAddress.
        @type: int  
        """
        self._ipAddress = ipAddress
        """
        @ivar: the ip address of InetAddress.
        @type: str  
        """
        self._port = port
        """
        @ivar: the port of InetAddress.
        @type: int  
        """
        
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