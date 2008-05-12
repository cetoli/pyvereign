from org.pyvereign.core.communication.endpoint.protocol.EndpointProtocol import EndpointProtocol
from org.pyvereign.util.Constants import Constants
from org.pyvereign.core.communication.endpoint.address.EndpointAddress import EndpointAddress

class AbstractEndpointProtocol(EndpointProtocol):
    """
    Description
    
    @author: Fabricio
    @since: 31/03/2008 - 15:05:58
    @version: 0.0.1
    """
    
    def init(self, networkProtocol, port, endpointService):
        """
        Initializes attributes of endpoint protocol.
        @rtype: None
        """
        self._networkProtocol = networkProtocol
        """
        @param: the network protocol used by endpoint protocol.
        @type: L{NetworkProtocol}  
        """
        self._port = port
        """
        @param: the port for communication.
        @type: int 
        """
        self._endpointService = endpointService
        """
        @param: reference for endpoint service
        @type: L{EndpointService} 
        """
        
    def getPort(self):
        return self._port
    
    def getPublicAddress(self):
        if not self._endpointService.getOwner():
            raise RuntimeError()
        communicationServer = self._endpointService.getOwner()
        if not communicationServer.getOwner():
            raise RuntimeError()
        microkernel = communicationServer.getOwner()
        if not microkernel.hasModule(Constants.ENVIRONMENT):
            raise RuntimeError()
        environment = microkernel.getModule(Constants.ENVIRONMENT)
        if not environment.hasModule(Constants.NETWORKING_SERVICE):
            raise RuntimeError()
        service = environment.getModule(Constants.NETWORKING_SERVICE)
        
        hostAddress = service.getHostAddress()
        return EndpointAddress(self._networkProtocol.getName(), hostAddress, self._port)
    
    def getMessageSender(self, endpointAddress):
        pass
    
        