from atlas.api.com.endpoint.service.EndpointService import EndpointService
from atlas.api.com.AbstractCommunicationService import AbstractCommunicationService
from atlas.api.com.endpoint.listener.EndpointListener import EndpointListener

class AbstractEndpointService(EndpointService, AbstractCommunicationService):
    
    def initialize(self, communication):
        AbstractCommunicationService.initialize(self, communication)
        self._name = "endpoint"
        self._endpointListeners = {}
    
    def addEndpointListener(self, uri, listener):
        if not uri:
            raise RuntimeError("uri is none.")
        if not isinstance(uri, str):
            raise TypeError("uri is not an instance of str class.")
        
        if not listener:
            raise RuntimeError("listener is none.")
        if not isinstance(listener, EndpointListener):
            raise TypeError("listener is not an instance of EndpointListener class.")
        self._endpointListeners[uri] = listener
        return listener
    
    def removeEndpointListener(self, uri):
        if not uri:
            raise RuntimeError("uri is none.")
        if not isinstance(uri, str):
            raise TypeError("uri is not an instance of str class.")
        listener = self._endpointListeners[uri]
        del self._endpointListeners[uri]
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