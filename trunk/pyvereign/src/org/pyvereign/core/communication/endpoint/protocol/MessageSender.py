class MessageSender(object):
    """
    Defines operations of message sender interface.
    
    @author: Fabricio
    @since: 31/03/2008 - 15:05:58
    @version: 0.0.1
    """
    
    def __init__(self):
        raise NotImplementedError()
    
    def sendMessage(self, message, timeout = 0):
        pass
    
    def getEndpointAddress(self):
        pass
    
    
    