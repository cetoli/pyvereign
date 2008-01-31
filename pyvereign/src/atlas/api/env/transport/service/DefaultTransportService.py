from atlas.api.env.transport.service.AbstractTransportService import AbstractTransportService

class DefaultTransportService(AbstractTransportService):
    
    def __init__(self):
        self.initialize()
        
    def initialize(self, *params):
        AbstractTransportService.initialize(self)