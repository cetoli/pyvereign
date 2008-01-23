from atlas.api.conf.InternalConfiguration import InternalConfiguration
class Microkernel(object):
    
    def __new__(cls):
        if not 'instance' in cls.__dict__:
            cls.instance = object.__new__(cls)
            cls.instance.initialize()
        return cls.instance 
    
    def initialize(self):
        self._internalServers = {}
        
        configuration = InternalConfiguration()
        
        self._internalServers["InternalConfiguration"] = configuration
        
        for intServer in self._internalServers.values():
            intServer.initialize()
    
    def start(self):
        for intServer in self._internalServers.values():
            intServer.start()
        
    def executeMecanism(self, internalServerName, serviceName, action, *params):
        internalServer = self._internalServers[internalServerName]
        return internalServer.executeService(serviceName, action, *params)