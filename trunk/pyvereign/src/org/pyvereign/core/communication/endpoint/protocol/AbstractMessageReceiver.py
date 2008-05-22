from org.pyvereign.core.communication.endpoint.protocol.MessageReceiver import MessageReceiver
from org.pyvereign.core.id.IDFactory import IDFactory
from org.pyvereign.util.Constants import Constants
from org.pyvereign.core.communication.endpoint.address.EndpointAddress import EndpointAddress
from org.pyvereign.core.communication.format.Format import Format

class AbstractMessageReceiver(MessageReceiver):
    
    def init(self, endpointAddress, format, kernel):
        if not isinstance(endpointAddress, EndpointAddress):
            raise TypeError()
        if not isinstance(format, Format):
            raise TypeError()
        self._endpointAddress = endpointAddress
        self._format = format
        self._kernel = kernel
        
    def getEndpointAddress(self):
        return self._endpointAddress
    
    def processStream(self, stream):
        self.receiveMessage(stream)
        
    def receiveMessage(self, stream):
        if not isinstance(stream, str):
            raise TypeError()
        try:
            message = self._format.unmarshal(stream)
            if not self._kernel.hasModule(IDFactory().createInternalServerID(Constants.COMMUNICATION)):
                raise RuntimeError()
            communication = self._kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION))
            if (communication.hasEndpointListener(message.getDestination().toURI())) and (self._endpointAddress.toURI() == message.getDestination().toURI()):
                listener = communication.getEndpointListener(message.getDestination().getURI())
                listener.processMessage(message)
        except:
            raise