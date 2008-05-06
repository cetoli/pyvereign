class EndpointListener(object):
    """
    Defines operations of EndpointListener interface.
    
    @author: Fabricio
    @since: 31/03/2008 - 15:05:58
    @version: 0.0.1
    """
    
    def __init__(self):
        raise NotImplementedError()
    
    def processMessage(self, message):
        """
        Process a message that arrives from stream.
        @param message: an EndpointMessage object.
        @type message: L{EndpointMessage}
        @rtype: None
        """
        pass
        
    