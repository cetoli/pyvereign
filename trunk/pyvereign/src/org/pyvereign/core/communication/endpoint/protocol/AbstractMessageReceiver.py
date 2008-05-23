from org.pyvereign.core.communication.endpoint.protocol.MessageReceiver import MessageReceiver
from org.pyvereign.core.id.IDFactory import IDFactory
from org.pyvereign.util.Constants import Constants
from org.pyvereign.core.communication.endpoint.address.EndpointAddress import EndpointAddress
from org.pyvereign.core.communication.format.FormatFactory import FormatFactory
from org.pyvereign.core.communication.format.FormatFactoryConfigurator import FormatFactoryConfigurator
from org.pyvereign.core.configuration.repository.ObjectRepository import ObjectRepository
from org.pyvereign.core.configuration.repository.ObjectRepositoryFactory import ObjectRepositoryFactory
from org.pyvereign.core.microkernel.Microkernel import Microkernel

class AbstractMessageReceiver(MessageReceiver):
    
    def init(self, endpointAddress, kernel):
        if not isinstance(endpointAddress, EndpointAddress):
            raise TypeError()
        if not isinstance(kernel, Microkernel):
            raise TypeError()
        self._endpointAddress = endpointAddress
        self._kernel = kernel
        
    def getEndpointAddress(self):
        return self._endpointAddress
    
    def processStream(self, stream):
        self.receiveMessage(stream)
        
    def receiveMessage(self, stream):
        if not isinstance(stream, str):
            raise TypeError()
        try:
            vector = stream.split(";")
            configurator = FormatFactoryConfigurator()
            configurator.setFilename(Constants.FORMAT_CONFIG_FILE)
            configurator.setObjectRepository(ObjectRepositoryFactory().createObjectRepository(Constants.DEFAULT_OBJECT_REPOSITORY))
            configurator.loadConfiguration()
            configurator.createObjects()
            factory = configurator.configureObject(FormatFactory())
            format = factory.createFormat(vector[1])
            message = format.unmarshal(vector[0])
            
            if not self._kernel.hasModule(IDFactory().createInternalServerID(Constants.COMMUNICATION)):
                raise RuntimeError()
            communication = self._kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION))
            if (communication.hasEndpointListener(message.getDestination().toURI())) and (self._endpointAddress.toURI() == message.getDestination().toURI()):
                listener = communication.getEndpointListener(message.getDestination().toURI())
                listener.processMessage(message)
                return message
            else:
                return
                
        except:
            raise