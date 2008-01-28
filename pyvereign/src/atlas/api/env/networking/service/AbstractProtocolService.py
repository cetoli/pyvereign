from atlas.api.env.networking.service.ProtocolService import ProtocolService
from atlas.api.env.networking.service.AbstractNetworkingService import AbstractNetworkingService
from sets import ImmutableSet

class AbstractProtocolService(ProtocolService, AbstractNetworkingService):
    
    def initialize(self, *params):
        AbstractNetworkingService.initialize(self)
        self._name = "protocol"
        self._protocols = {}
    
    def start(self, *params):
        if not self._dataSource:
            raise RuntimeError("Data source is none.")
        protocols = self._dataSource.retrieveProtocols()
        for p in protocols:
            self._protocols[p.getName()] = p
    
    def getProtocols(self):
        return ImmutableSet(self._protocols.values())
    
    def getProtocol(self, name):
        return self._protocols[name]