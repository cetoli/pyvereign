from atlas.api.env.transport.listener.StreamListener import StreamListener
from atlas.api.com.endpoint.address.EndpointAddress import EndpointAddress
from atlas.api.com.endpoint.format.MessageFormat import MessageFormat
from atlas.api.com.CommunicationService import CommunicationService

class MessageReceiver(StreamListener):
    
    def __init__(self, endpointAddress, format, service):
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
        
        if not service:
            raise RuntimeError("sevice parameter is none.")
        if not isinstance(service, CommunicationService):
            raise TypeError("service is not an instance of CommunicationService class.")
        self._service = service
        
    def receiveMessage(self, stream):
        try:
            message = self._format.unmarshal(stream)
            
        except:
            raise
    
    def processStream(self, stream):
        self.receiveMessage(stream)
        