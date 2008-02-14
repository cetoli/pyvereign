from atlas.api.env.hardware.service.AbstractMachineService import AbstractMachineService

class DefaultMachineService(AbstractMachineService):
    
    def __init__(self):
        self._name = ""
        
    def initialize(self, environment):
        AbstractMachineService.initialize(self, environment)
    
