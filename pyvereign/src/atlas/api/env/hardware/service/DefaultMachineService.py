from atlas.api.env.hardware.service.AbstractMachineService import AbstractMachineService

class DefaultMachineService(AbstractMachineService):
    
    def __init__(self):
        self._status = DefaultMachineService.NON_INITIALIZED
        
    
