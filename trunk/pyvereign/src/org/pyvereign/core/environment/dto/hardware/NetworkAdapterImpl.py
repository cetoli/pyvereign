from org.pyvereign.core.environment.dto.hardware.AbstractNetworkAdapter import AbstractNetworkAdapter

class NetworkAdapterImpl(AbstractNetworkAdapter):
    """
    Defines the default implementation of AbstractNetworkAdapter class. 
    
    @author: Fabricio
    @since: 30/03/2008 - 00:01:13
    @version: 0.0.1
    """
    
    def __init__(self, values):
        self.init(values)
    