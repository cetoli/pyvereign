from org.pyvereign.core.communication.endpoint.protocol.EndpointProtocol import EndpointProtocol

class AbstractEndpointProtocol(EndpointProtocol):
    """
    Description
    
    @author: Fabricio
    @since: 31/03/2008 - 15:05:58
    @version: 0.0.1
    """
    
    def init(self, networkProtocol, port, endpointService):
        """
        Initializes attributes of endpoint protocol.
        @rtype: None
        """
        self._networkProtocol = networkProtocol
        """
        @param: the network protocol used by endpoint protocol.
        @type: L{NetworkProtocol}  
        """
        self._port = port
        """
        @param: the port for communication.
        @type: int 
        """
        self._endpointService = endpointService
        """
        @param: reference for endpoint service
        @type: L{EndpointService} 
        """
        
    def getPort(self):
        return self._port
    
    def getPublicAddress(self):
        pass
        
    
        