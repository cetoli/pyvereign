from atlas.api.com.endpoint.service.EndpointService import EndpointService
from atlas.api.com.AbstractCommunicationService import AbstractCommunicationService
from atlas.api.com.endpoint.listener.EndpointListener import EndpointListener
from atlas.api.com.endpoint.address.EndpointAddress import EndpointAddress
from atlas.api.com.endpoint.format.JSONMessageFormat import JSONMessageFormat
from atlas.api.com.endpoint.message.EndpointMessage import EndpointMessage
from atlas.api.com.endpoint.protocol.EndpointProtocol import EndpointProtocol
from atlas.api.com.endpoint.format.MessageFormat import MessageFormat
from sets import ImmutableSet

class AbstractEndpointService(EndpointService, AbstractCommunicationService):
    
    def initialize(self, communication):
        AbstractCommunicationService.initialize(self, communication)
        self._endpointListeners = {}
        self._endpointProtocols = {}
        
        from atlas.api.microkernel.Microkernel import Microkernel
        
        protocols = Microkernel().executeMecanism("Environment", "transport", "getProtocols")
        
        for p in protocols:
            self._endpointProtocols[p.getName()] = EndpointProtocol(p)
    
    def addEndpointListener(self, uri, listener):
        if not uri:
            raise RuntimeError("uri is none.")
        if not isinstance(uri, str):
            raise TypeError("uri is not an instance of str class.")
        
        if not listener:
            raise RuntimeError("listener is none.")
        if not isinstance(listener, EndpointListener):
            raise TypeError("listener is not an instance of EndpointListener class.")
        
        addr = EndpointAddress.toEndpointAddress(uri)
        from atlas.api.microkernel.Microkernel import Microkernel
        receiver = self._endpointProtocols[addr.getProtocol()].getMessageReceiver(addr, JSONMessageFormat(), self)
        Microkernel().executeMecanism("Environment", "transport", "addTransportListener", addr.getProtocol(), uri, receiver)
        
        self._endpointListeners[uri] = listener
        return listener
    
    def getNumberOfEndpointListeners(self):
        return len(self._endpointListeners)
    
    def removeEndpointListener(self, uri):
        if not uri:
            raise RuntimeError("uri is none.")
        if not isinstance(uri, str):
            raise TypeError("uri is not an instance of str class.")
        listener = self._endpointListeners[uri]
        del self._endpointListeners[uri]
        addr = EndpointAddress.toEndpointAddress(uri)
        from atlas.api.microkernel.Microkernel import Microkernel
        Microkernel().executeMecanism("Environment", "transport", "removeTransportListener", addr.getProtocol(), uri)
        return listener
    
    def getEndpointListener(self, uri):
        if not uri:
            raise RuntimeError("uri is none.")
        if not isinstance(uri, str):
            raise TypeError("uri is not an instance of str class.")
        return self._endpointListeners[uri]
    
    def hasEndpointListener(self, uri):
        if not uri:
            raise RuntimeError("uri is none.")
        if not isinstance(uri, str):
            raise TypeError("uri is not an instance of str class.")
        return self._endpointListeners.has_key(uri)
    
    def createEndpointMessage(self, origin, destination, event = None):
        if not origin:
            raise RuntimeError("origin is none.")
        if not isinstance(origin, str):
            raise TypeError("origin is not an instance of str class.")
        if not destination:
            raise RuntimeError("destination is none.")
        if not isinstance(destination, str):
            raise TypeError("destination is not an instance of str class.")
        addrOrigin = EndpointAddress.toEndpointAddress(origin)
        addrDestination = EndpointAddress.toEndpointAddress(destination)
        return EndpointMessage(addrOrigin, addrDestination, event)
    
    def createEndpointAddress(self, uri):
        if not uri:
            raise RuntimeError("uri is none.")
        if not isinstance(uri, str):
            raise TypeError("uri is not an instance of str class.")
        return EndpointAddress.toEndpointAddress(uri)
    
    def getMessageSender(self, endpointAddress, format):
        if not endpointAddress:
            raise RuntimeError("endpointAddress is none.")
        if not isinstance(endpointAddress, EndpointAddress):
            raise TypeError("endpointAddress is not an instance of EndpointAddress class.")
        if not format:
            raise RuntimeError("format is none.")
        if not isinstance(format, MessageFormat):
            raise TypeError("format is not an instance of MessageFormat class.")
        return self._endpointProtocols[endpointAddress.getProtocol()].getMessageSender(endpointAddress, format)
    
    def getProtocolByName(self, protocolName):
        if not protocolName:
            raise RuntimeError("protocolName is none.")
        if not isinstance(protocolName, str):
            raise TypeError("protocolName is not an instance of str class.")
        return self._endpointProtocols[protocolName]
    
    def getEndpointProtocols(self):
        return ImmutableSet(self._endpointProtocols.values())