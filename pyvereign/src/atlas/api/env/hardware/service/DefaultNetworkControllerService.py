from atlas.api.env.hardware.service.AbstractNetworkControllerService import AbstractNetworkControllerService

class DefaultNetworkControllerService(AbstractNetworkControllerService):
    
    def __init__(self):
        self._status = DefaultNetworkControllerService.NON_INITIALIZED
        
    def initialize(self, environment):
        AbstractNetworkControllerService.initialize(self, environment)
        
    