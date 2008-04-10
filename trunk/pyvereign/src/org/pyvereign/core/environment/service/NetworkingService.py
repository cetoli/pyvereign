from org.pyvereign.core.platform.Service import Service

class NetworkingService(Service):
    """
    Defines the interface of networking services.
    
    @author: Fabricio
    @since: 31/03/2008 - 15:05:58
    @version: 0.0.1
    """
    
    def __init__(self):
        raise NotImplementedError()
    
    def getNetworkProtocols(self):
        """
        Gets a list of network protocols.
        @return: Returns a list of network protocols.
        @rtype: ImmutableSet
        """
        pass
    