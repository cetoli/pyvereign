from org.pyvereign.core.platform.Service import Service

class EndpointService(Service):
    """
    Defines operations of endpoint service interface.
    
    @author: Fabricio
    @since: 31/03/2008 - 15:05:58
    @version: 0.0.1
    """
    
    def __init__(self):
        raise NotImplementedError()
    
    def addEndpointListener(self, uri, listener):
        pass
    
    def removeEndpointListener(self, uri):
        pass
    
    def getEndpointListener(self, uri):
        pass