from atlas.api.microkernel.InternalServer import InternalServer

class AbstractInternalServer(InternalServer):
    
    def initialize(self, *params):
        self._services = {}
        self._status = InternalServer.INITIALIZED
    
    def executeService(self, serviceName, action, *params):
        return self._services[serviceName].__getattribute__(action)(*params)
    
    def registerService(self, name, service):
        self._services[name] = service
        return self._services[name]
    
    def unregisterService(self, name):
        service = self._services[name]
        del self._services[name]
        return service
    
    def clearServices(self):
        self._services.clear()
        
    def start(self, *params):
        self._status = InternalServer.STARTED
        
    def stop(self):
        self._status = InternalServer.STOPED