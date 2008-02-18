from atlas.api.env.transport.listener.StreamListener import StreamListener
from atlas.api.com.endpoint.address.EndpointAddress import EndpointAddress
from atlas.api.com.endpoint.format.MessageFormat import MessageFormat

class MessageReceiver(StreamListener):
    
    def __init__(self, endpointAddress, format):
        if not endpointAddress:
            raise RuntimeError("endpointAddress parameter is none.")
        if not isinstance(endpointAddress, EndpointAddress):
            raise TypeError("endpointAddress parameter is not an instance of EndpointAddress class.")
        self._endpointAddress = endpointAddress
        
        if not format:
            raise RuntimeError("format parameter is none.")
        if not isinstance(format, MessageFormat):
            raise TypeError("format parameter is not an instance of MessageFormat class.")
        self._format = format
        
    def receiveMessage(self, stream):
        pass
    
    def processStream(self, stream):
        self.receiveMessage(stream)
        