from atlas.api.com.endpoint.service.EndpointService import EndpointService
from atlas.api.com.AbstractCommunicationService import AbstractCommunicationService

class AbstractEndpointService(EndpointService, AbstractCommunicationService):
    
    def initialize(self, communication):
        AbstractCommunicationService.initialize(self, communication)
        self._name = "endpoint"
        self._endpointListeners = {}
    
    def addEndpointListener(self, uri, listener):
        self._endpointListeners[uri] = listener
        return listener
    
    def removeEndpointListener(self, uri):
        listener = self._endpointListeners[uri]
        del self._endpointListeners[uri]
        return listener
    
    def getEndpointListener(self, uri):
        return self._endpointListeners[uri]