from atlas.api.microkernel.AbstractInternalServer import AbstractInternalServer
from atlas.api.conf.service.ConfigurationService import ConfigurationService

class InternalConfiguration(AbstractInternalServer):
    
    def __init__(self):
        self.initialize()
    
    def initialize(self, *params):
        AbstractInternalServer.initialize(self)
        
        configurationService = ConfigurationService()
        
        self._services[configurationService.getName()] = configurationService
        
    