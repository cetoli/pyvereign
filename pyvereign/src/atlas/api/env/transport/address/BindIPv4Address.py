from atlas.api.env.transport.address.IPv4Address import IPv4Address

class BindIPv4Address(IPv4Address):
    
    def __init__(self, port):
        IPv4Address.__init__(self, '', port)
        
    def getIPAddress(self):
        return "127.0.0.1"
        
    def isBindAddress(self):
        return True
    
    def getTuple(self):
        return "127.0.0.1", self._port