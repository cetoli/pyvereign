from atlas.api.env.networking.service.ProtocolService import ProtocolService
from atlas.api.env.networking.service.AbstractNetworkingService import AbstractNetworkingService
from sets import ImmutableSet

class AbstractProtocolService(ProtocolService, AbstractNetworkingService):
    
    def initialize(self, environment):
        self._name = "protocol"
        self._protocols = {}
        if not self._dataSource:
            raise RuntimeError("Data source is none.")
        protocols = self._dataSource.retrieveProtocols()
        for p in protocols:
            self._protocols[p.getName()] = p
        AbstractNetworkingService.initialize(self, environment)
        
    def getProtocols(self):
        return ImmutableSet(self._protocols.values())
    
    def getProtocol(self, name):
        return self._protocols[name]
    
    def hasProtocol(self, name):
        return self._protocols.has_key(name)