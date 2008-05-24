from org.pyvereign.core.environment.transport.listener.TransportListener import TransportListener

class MessageReceiver(TransportListener):
    
    def __init__(self):
        raise NotImplementedError()
    
    def receiveMessage(self, stream):
        pass
    
    def getEndpointAddress(self):
        pass