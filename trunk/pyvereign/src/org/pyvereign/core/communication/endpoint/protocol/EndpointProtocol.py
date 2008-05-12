class EndpointProtocol(object):
    """
    Defines the interface with all operations for message transport proctocols.
    
    @author: Fabricio
    @since: 31/03/2008 - 15:05:58
    @version: 0.0.1
    """
    
    def __init__(self):
        raise NotImplementedError()
    
    def getName(self):
        """
        Gets the name of protocol.
        @return: Returns the name of protocol.
        @rtype: str
        """
        pass
    
    def getPublicAddress(self):
        """
        Gets the public endpoint address.
        @return: Returns the public endpoint address.
        @rtype: L{EndpointAddress}
        """
        pass
    
    def getMessageSender(self, endpointAddress):
        """
        Gets a sender of endpoint message.
        
        @param endpointAddress: the address for sending.
        @type endpointAddress: L{EndpointAddress}
        @return: Returns a sender of endpoint message.
        @rtype: L{MessageSender}
        """
        pass
    
    def getMessageReceiver(self, endpointAddress):
        """
        Gets a receiver of endpoint message.
        
        @param endpointAddress: the address for recieving.
        @type endpointAddress: L{EndpointAddress}
        @return: Returns a receiver of endpoint message.
        @rtype: L{MessageReceiver}
        """
        pass
    
    def getPort(self):
        """
        Gets the port of message transport protocol.
        @return: Returns the port of message transport protocol.
        @rtype: rtype
        """
        pass
        
        
    
        