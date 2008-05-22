class Format(object):
    """
    Defines the interface for message formarts.
    
    @author: Fabricio
    @since: 31/03/2008 - 15:05:58
    @version: 0.0.1
    """
    
    def __init__(self):
        raise NotImplementedError()
    
    def getName(self):
        pass
    
    def marshal(self, object):
        """
        Converts an message for a specific message.
        @return: Returns an message for a specific message.
        @rtype: str
        """
        pass
    
    def unmarshal(self, stream):
        """
        Converts an stream for a EndpointMessage object.
        @return: Returns an stream for a EndpointMessage object.
        @rtype: L{EndpointMessage}
        """
        pass
    