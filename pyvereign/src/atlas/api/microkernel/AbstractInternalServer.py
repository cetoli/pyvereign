from atlas.api.microkernel.InternalServer import InternalServer

class AbstractInternalServer(InternalServer):
    
    def initialize(self, *params):
        self._services = {}
    
    def executeService(self, serviceName, action, *params):
        return self._services[serviceName].__getattribute__(action)(*params)