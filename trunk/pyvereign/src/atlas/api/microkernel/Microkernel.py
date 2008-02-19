from atlas.api.env.Environment import Environment

class Microkernel(object):
    
    NON_INITIALIZED = 0
    INITIALIZED = 1
    STARTED = 2
    STOPED = 3
    
    def __new__(cls):
        if not 'instance' in cls.__dict__:
            cls.instance = object.__new__(cls)
            cls.instance._status = cls.NON_INITIALIZED
        return cls.instance 
    
    def initialize(self):
        if self._status == Microkernel.NON_INITIALIZED:
            self._internalServers = {}
            
            environment = Environment()
            self._internalServers["Environment"] = environment
            
            for intServer in self._internalServers.values():
                intServer.initialize()
                
            self._status = Microkernel.INITIALIZED
    
    def start(self):
        if self._status == Microkernel.INITIALIZED:
            for intServer in self._internalServers.values():
                intServer.start()
            
            self._status = Microkernel.STARTED
    
    def stop(self):
        if self._status == Microkernel.STARTED:
            for intServer in self._internalServers.values():
                intServer.start()
            
            self._status = Microkernel.STOPED
            
    def executeMecanism(self, internalServerName, serviceName, action, *params):
        internalServer = self._internalServers[internalServerName]
        return internalServer.executeService(serviceName, action, *params)
    
    def getStatus(self):
        return self._status
    
