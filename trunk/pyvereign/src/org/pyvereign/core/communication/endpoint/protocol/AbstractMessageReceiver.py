from org.pyvereign.core.communication.endpoint.protocol.MessageReceiver import MessageReceiver

class AbstractMessageReceiver(MessageReceiver):
    
    def init(self, endpointAddress, format, kernel):
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
            #teste
        except:
            raise