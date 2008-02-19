from atlas.api.microkernel.Microkernel import Microkernel
from atlas.api.com.endpoint.address.EndpointAddress import EndpointAddress
from atlas.api.com.endpoint.listener.EndpointListener import EndpointListener

class EndpointListenerForTest(EndpointListener):
    
    def __init__(self):
        self._message = None
        self._count = 0
        
    def processMessage(self, message):
        self._message = message
        print message.getDestination().toURI()


Microkernel().initialize()
Microkernel().start(5052)

addr1 = EndpointAddress("TCP", "127.0.0.1", 5052)
addr2 = EndpointAddress("TCP", "127.0.0.1", 5052, "service")



Microkernel().executeMecanism("Communication", "endpoint", "addEndpointListener", addr1.toURI(), EndpointListenerForTest())
Microkernel().executeMecanism("Communication", "endpoint", "addEndpointListener", addr2.toURI(), EndpointListenerForTest())


