from atlas.api.com.ipc.service.AbstractIPCService import AbstractIPCService

class DefaultIPCService(AbstractIPCService):
    
    def __init__(self):
        self._status = DefaultIPCService.NON_INITIALIZED
        
    def initialize(self, communication):
        AbstractIPCService.initialize(self, communication)
        
    
        