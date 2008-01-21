from atlas.api.env.service.AbstractMachineService import AbstractMachineService

class DefaultMachineService(AbstractMachineService):
    
    def __init__(self):
        self.initialize()
        
    def initialize(self, *params):
        AbstractMachineService.initialize(self)