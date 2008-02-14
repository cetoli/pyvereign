from atlas.api.env.transport.service.TransportService import TransportService
from atlas.api.env.AbstractEnvironmentService import AbstractEnvironmentService

class AbstractTransportService(TransportService, AbstractEnvironmentService):
    
    def initialize(self, environment):
        AbstractEnvironmentService.initialize(self, environment)
        self._name = "transport"