from org.pyvereign.core.environment.transport.address.IPv4Address import IPv4Address

class BroadcastIPv4Address(IPv4Address):
    
    def __init__(self, port):
        IPv4Address.__init__(self, '<broadcast>', port)
        
    def isBroadcastAddress(self):
        return True