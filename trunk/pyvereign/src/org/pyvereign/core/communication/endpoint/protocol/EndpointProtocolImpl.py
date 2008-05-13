from org.pyvereign.core.communication.endpoint.protocol.AbstractEndpointProtocol import AbstractEndpointProtocol

class EndpointProtocolImpl(AbstractEndpointProtocol):
    """
    Defines a concrete implementation for EndpointProtocol.
    
    @author: Fabricio
    @since: 31/03/2008 - 15:05:58
    @version: 0.0.1
    """
    
    def __init__(self, networkProtocol):
        self.init(networkProtocol)
    