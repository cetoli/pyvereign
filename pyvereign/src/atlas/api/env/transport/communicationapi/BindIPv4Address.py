from atlas.api.env.transport.communicationapi.IPv4Address import IPv4Address

class BindIPv4Address(IPv4Address):
    
    def __init__(self, port):
        IPv4Address.__init__(self, '127.0.0.1', port)