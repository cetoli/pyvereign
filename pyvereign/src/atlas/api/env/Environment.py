from atlas.api.microkernel.InternalServer import InternalServer

class Environment(InternalServer):
    
    def __init__(self):
        self._services = {}

    def executeService(self, serviceName, action, *params):
        return self._services[serviceName].__getattribute__(action)(*params)
    
    def initialize(self, *params):
        pass

