from org.pyvereign.core.environment.instrumentation.dto.networking.AbstractNetworkProtocol import AbstractNetworkProtocol

class NetworkProtocolImpl(AbstractNetworkProtocol):
    """
    Defines the default implementation of AbstractNetworkProtocol class. 
    
    @author: Fabricio
    @since: 31/03/2008 - 15:05:58
    @version: 0.0.1
    """
    
    def __init__(self, values):
        self.init(values)
    