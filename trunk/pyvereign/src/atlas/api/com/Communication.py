from atlas.api.microkernel.AbstractInternalServer import AbstractInternalServer
from atlas.api.com.endpoint.service.DefaultEndpointService import DefaultEndpointService
from atlas.api.com.ipc.service.DefaultIPCService import DefaultIPCService

class Communication(AbstractInternalServer):
    
    def __init__(self):
        oi = 1
        
    def initialize(self, *params):
        AbstractInternalServer.initialize(self, *params)
        self._services["endpoint"] = DefaultEndpointService()
        self._services["ipc"] = DefaultIPCService()
        
        for s in self._services.values():
            s.initialize(self)
            
    def start(self, *params):
        for s in self._services.values():
            s.start(*params)