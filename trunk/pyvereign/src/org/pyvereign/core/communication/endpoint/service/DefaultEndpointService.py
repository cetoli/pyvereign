from org.pyvereign.core.communication.endpoint.service.AbstractEndpointService import AbstractEndpointService
from org.pyvereign.core.id.IDFactory import IDFactory
from org.pyvereign.util.Constants import Constants
from org.pyvereign.core.communication.endpoint.protocol.EndpointProtocolCreator import EndpointProtocolCreator
from org.pyvereign.core.communication.endpoint.address.EndpointAddress import EndpointAddress
from org.pyvereign.core.communication.endpoint.listener.EndpointListener import EndpointListener
from org.pyvereign.core.communication.endpoint.message.EndpointMessage import EndpointMessage
from sets import ImmutableSet
from org.pyvereign.core.exception.EndpointServiceError import EndpointServiceError

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
        if not isinstance(uri, str):
            raise TypeError()
        if not isinstance(listener, EndpointListener):
            raise TypeError()
        addr = EndpointAddress.getEndpointAddress(uri)
        kernel = self._owner.getOwner()
        environment = kernel.getModule(IDFactory().createInternalServerID(Constants.ENVIRONMENT))
        endpointProtocol = self._endpointProtocols[addr.getProtocol()]
        
        receiver = endpointProtocol.getMessageReceiver(addr, kernel)
        environment.addTransportListener(addr.getProtocol(), uri, receiver)
        self._endpointListeners[uri] = listener
        return listener
    
    def removeEndpointListener(self, uri):
        if not isinstance(uri, str):
            raise TypeError()
        addr = EndpointAddress.getEndpointAddress(uri)
        kernel = self._owner.getOwner()
        environment = kernel.getModule(IDFactory().createInternalServerID(Constants.ENVIRONMENT))
        
        environment.removeTransportListener(addr.getProtocol(), uri)
        listener = self._endpointListeners[uri]
        del self._endpointListeners[uri]
        return listener
    
    def getEndpointListener(self, uri):
        if not isinstance(uri, str):
            raise TypeError()
        return self._endpointListeners[uri]
    
    def hasEndpointListener(self, uri):
        if not isinstance(uri, str):
            raise TypeError()
        return self._endpointListeners.has_key(uri)
    
    def createEndpointMessage(self, origin, destination, event = None):
        if not isinstance(origin, str):
            raise TypeError()
        if not isinstance(destination, str):
            raise TypeError()
        return EndpointMessage(EndpointAddress.getEndpointAddress(origin), EndpointAddress.getEndpointAddress(origin), event)
    
    def createEndpointAddress(self, uri):
        return EndpointAddress.getEndpointAddress(uri)
    
    def getMessageSender(self, uri):
        if not isinstance(uri, str):
            raise TypeError()
        endpointAddress = EndpointAddress.getEndpointAddress(uri)
        return self._endpointProtocols[endpointAddress.getProtocol()].getMessageSender(endpointAddress, self._owner.getOwner())
    
    def getEndpointProtocolByName(self, name):
        if not isinstance(name, str):
            raise TypeError()
        if not self._endpointProtocols.has_key(name):
            raise EndpointServiceError()
        return self._endpointProtocols[name]
    
    def getEndpointProtocols(self):
        return ImmutableSet(self._endpointProtocols.values())