from org.pyvereign.core.environment.transport.address.IPv4Address import IPv4Address

class BroadcastIPv4Address(IPv4Address):
    """
    Defines the impletation of broadcast address for IPv4Address.
    @author: Fabricio
    @since: 
    @version: 0.0.1
    """
    
    def __init__(self, port):
        IPv4Address.__init__(self, '<broadcast>', port)
        
    def isBroadcastAddress(self):
        return True