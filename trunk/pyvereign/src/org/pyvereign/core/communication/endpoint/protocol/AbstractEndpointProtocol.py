from org.pyvereign.core.communication.endpoint.protocol.EndpointProtocol import EndpointProtocol
from org.pyvereign.core.environment.instrumentation.dto.networking.NetworkProtocol import NetworkProtocol
from org.pyvereign.core.communication.endpoint.protocol.MessageSenderCreator import MessageSenderCreator
from org.pyvereign.core.communication.format.Format import Format
from org.pyvereign.core.communication.endpoint.address.EndpointAddress import EndpointAddress

class AbstractEndpointProtocol(EndpointProtocol):
    """
    Description
    
    @author: Fabricio
    @since: 31/03/2008 - 15:05:58
    @version: 0.0.1
    """
    
    def init(self, networkProtocol):
        """
        Initializes attributes of endpoint protocol.
        @rtype: None
        """
        if not isinstance(networkProtocol, NetworkProtocol):
            raise TypeError()
        self._networkProtocol = networkProtocol
        """
        @param: the network protocol used by endpoint protocol.
        @type: L{NetworkProtocol}  
        """
    
    def getName(self):
        return self._networkProtocol.getName()

    def getMessageSender(self, endpointAddress, kernel):
        if not isinstance(endpointAddress, EndpointAddress):
            raise TypeError()
        from org.pyvereign.core.microkernel.Microkernel import Microkernel
        if not isinstance(kernel, Microkernel):
            raise TypeError()
        return MessageSenderCreator.createMessageSender(endpointAddress, kernel)