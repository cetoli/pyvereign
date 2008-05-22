from org.pyvereign.core.communication.endpoint.service.AbstractEndpointService import AbstractEndpointService
from org.pyvereign.core.id.IDFactory import IDFactory
from org.pyvereign.util.Constants import Constants
from org.pyvereign.core.communication.endpoint.protocol.EndpointProtocolCreator import EndpointProtocolCreator

class DefaultEndpointService(AbstractEndpointService):
    
    def __init__(self):
        self.init()
        
    def initialize(self, owner, id, context):
        AbstractEndpointService.initialize(self, owner, id, context)
        
        kernel = self._owner.getOwner()
        environment = kernel.getModule(IDFactory().createInternalServerID(Constants.ENVIRONMENT))
        
        protocols = environment.getNetworkProtocols()
        
        for p in protocols:
            endpointProtocol = EndpointProtocolCreator.createEndpointProtocol(p)
            self._endpointProtocols[endpointProtocol.getName()] = endpointProtocol
            
    def addEndpointListener(self, uri, listener):
        pass
    
    def removeEndpointListener(self, uri):
        pass
    
    def getEndpointListener(self, uri):
        pass
    
    def hasEndpointListener(self, uri):
        pass