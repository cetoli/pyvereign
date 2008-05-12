class MessageSender(object):
    """
    Defines operations of message sender interface.
    
    @author: Fabricio
    @since: 31/03/2008 - 15:05:58
    @version: 0.0.1
    """
    
    def __init__(self):
        raise NotImplementedError()
    
    def sendMessage(self, endpointMessage, formatType):
        """
        Sends a message over a network.
        
        @param endpointMessage: a EndpointMessage object.
        @type endpointMessage: L{EndpointMessage}
        @param formatType: the type of format.
        @type formatType: str
        @return: Returns a message over a network.
        @rtype: L{EndpointMessage}
        """
        pass
    