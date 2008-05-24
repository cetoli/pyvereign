class TransportListener(object):
    """
    Defines the common interface for transport listener objects.
    
    @author: Fabricio
    @since: 19/01/2008 - 10:19:10
    @version: 0.0.1
    """
    
    def __init__(self):
        raise NotImplementedError()
    
    def processStream(self, stream):
        """
        Processes a stream.
        @param stream: a stream.
        @type stream: str
        @rtype: None
        """
        pass