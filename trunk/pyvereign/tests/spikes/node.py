from org.pyvereign.core.communication.endpoint.listener.EndpointListener import EndpointListener
from org.pyvereign.core.microkernel.Microkernel import Microkernel
from org.pyvereign.core.id.IDFactory import IDFactory
from org.pyvereign.util.Constants import Constants
from org.pyvereign.core.communication.endpoint.address.EndpointAddress import EndpointAddress

class EndpointListenerForTest(EndpointListener):
    
    def __init__(self):
        return
    
    def processMessage(self, message):
        print message.getDestination().toURI()
        
        
kernel = Microkernel()
kernel.initialize()
kernel.start([5052])

communication = kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION))
communication.addEndpointListener(EndpointAddress("TCP", "127.0.0.1", 5052).toURI(), EndpointListenerForTest())
communication.addEndpointListener(EndpointAddress("UDP", "127.0.0.1", 5052).toURI(), EndpointListenerForTest())
communication.addEndpointListener(EndpointAddress("TCP", "127.0.0.1", 5052, "service").toURI(), EndpointListenerForTest())
communication.addEndpointListener(EndpointAddress("UDP", "127.0.0.1", 5052, "service").toURI(), EndpointListenerForTest())
communication.addEndpointListener(EndpointAddress("TCP", "127.0.0.1", 5052, "service", "action").toURI(), EndpointListenerForTest())
communication.addEndpointListener(EndpointAddress("UDP", "127.0.0.1", 5052, "service", "action").toURI(), EndpointListenerForTest())
communication.addEndpointListener(EndpointAddress("TCP", "127.0.0.1", 5052, "service", "action", "parameter").toURI(), EndpointListenerForTest())
communication.addEndpointListener(EndpointAddress("UDP", "127.0.0.1", 5052, "service", "action", "parameter").toURI(), EndpointListenerForTest())

