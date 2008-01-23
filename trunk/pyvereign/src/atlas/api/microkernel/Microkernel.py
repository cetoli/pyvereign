class Microkernel(object):
    
    def __new__(cls):
        if not 'instance' in cls.__dict__:
            cls.instance = object.__new__(cls)
            cls.instance.initialize()
        return cls.instance 
    
    def initialize(self):
        self._internalServers = {}
        
    def executeMecanism(self, internalServerName, serviceName, action, *params):
        internalServer = self._internalServers[internalServerName]
        return internalServer.executeService(serviceName, action, *params)