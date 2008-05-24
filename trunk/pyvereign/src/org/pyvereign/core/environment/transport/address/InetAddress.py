class InetAddress(object):
    """
    Defines the common interface of InetAddress objects.
    @author: Fabricio
    @since: 
    @version: 0.0.1
    """
    
    def __init__(self):
        raise NotImplementedError()
    
    def getFamily(self):
        """
        Gets the family of inetaddress.
        @return: Returns the family of inetaddress.
        @rtype: int
        """
        pass
    
    def getIPAddress(self):
        """
        Gets the ip address.
        @return: Returns the ip address.
        @rtype: str
        """
        pass
    
    def getPort(self):
        """
        Gets the port number of inetaddres.
        @return: Returns the port number of inetaddres.
        @rtype: int
        """
        pass
    
    def getTuple(self):
        """
        Creates a tuple object with inetaddress ipaddress and port.
        @return: Returns a tuple object with inetaddress ipaddress and port.
        @rtype: tuple
        """
        pass
    
    def isBroadcastAddress(self):
        """
        Verifies if an inet address is a broadcast address.
        @return: Returns true if an inet address is a broadcast address.
        @rtype: bool
        """
        pass
    
    def isBindAddress(self):
        """
        Verifies if an inet address is a bind address.
        @return: Returns true if an inet address is a bind address.
        @rtype: bool
        """
        pass
    
    def setPort(self, port):
        """
        Sets the port of inet address.
        @return: Returns the port of the inetaddress.
        @rtype: int
        """
        pass