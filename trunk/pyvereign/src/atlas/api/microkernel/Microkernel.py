from atlas.api.conf.InternalConfiguration import InternalConfiguration

class Microkernel(object):
    
    NON_UNITIALIZED = 0
    INITIALIZED = 1
    STARTED = 2
    STOPED = 3
    
    def __new__(cls):
        if not 'instance' in cls.__dict__:
            cls.instance = object.__new__(cls)
            cls.instance._status = cls.NON_UNITIALIZED
        return cls.instance 
    
    def initialize(self):
        self._internalServers = {}
        
        configuration = InternalConfiguration()
        
        self._internalServers["InternalConfiguration"] = configuration
        
        for intServer in self._internalServers.values():
            intServer.initialize()
            
        self._status = Microkernel.INITIALIZED
    
    def start(self):
        for intServer in self._internalServers.values():
            intServer.start()
        
        self._status = Microkernel.STARTED
        
    def executeMecanism(self, internalServerName, serviceName, action, *params):
        internalServer = self._internalServers[internalServerName]
        return internalServer.executeService(serviceName, action, *params)
    
    def getStatus(self):
        return self._status
    
