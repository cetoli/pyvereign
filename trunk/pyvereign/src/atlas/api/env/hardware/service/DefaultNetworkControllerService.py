from atlas.api.env.hardware.service.AbstractNetworkControllerService import AbstractNetworkControllerService

class DefaultNetworkControllerService(AbstractNetworkControllerService):
    
    def __init__(self):
        self.initialize()
    
    def initialize(self, *params):
        AbstractNetworkControllerService.initialize(self)
        
    