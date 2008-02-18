from atlas.api.env.networking.Protocol import Protocol

class EndpointProtocol(object):
    
    def __init__(self, protocol):
        if not protocol:
            raise RuntimeError("The protocol parameter is none.")
        if not isinstance(protocol, Protocol):
            raise TypeError("The protocol parameter is not an instance of Protocol class.")
        self._protocol = protocol
        
    def getMessageSender(self, address, messageFormat):
        if not address:
            raise RuntimeError("address parameter is none.")
        if not messageFormat:
            raise RuntimeError("messageFormat parameter is none.")
    
    def getMessageReceiver(self, address, messageFormat):
        if not address:
            raise RuntimeError("address parameter is none.")
        if not messageFormat:
            raise RuntimeError("messageFormat parameter is none.") 