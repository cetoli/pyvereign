class NetworkProtocol(object):
    """
    Defines the interface for network protocols. 
    
    @author: Fabricio
    @since: 30/03/2008 - 20:32:27
    @version: 0.0.1
    """
    
    def getName(self):
        """
        Gets the name of protocol.
        @return: Returns the name of protocol.
        @rtype: str
        """
        pass
    
    def supportsBroadcasting(self):
        """
        Gets if protocol supports broadcast operation.
        @return: Returns if protocol supports broadcast operation.
        @rtype: bool
        """
        pass
    
    def guaranteesDelivery(self):
        """
        Verifies if protocol offers guarantee of delivery.
        @return: Returns if protocol offers guarantee of delivery.
        @rtype: bool
        """
        pass
    
    def supportsMulticasting(self):
        """
        Gets if protocol supports multicast operation.
        @return: Returns if protocol supports broadcast operation.
        @rtype: bool
        """
        pass
    
    
    