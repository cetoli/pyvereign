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
    
    def initialize(self, *params):
        if self._status == Microkernel.NON_INITIALIZED:
            self._internalServers = {}
            
            self._internalServers["Environment"] = Environment()
            from atlas.api.com.Communication import Communication
            self._internalServers["Communication"] = Communication()
            
            for intServer in self._internalServers.values():
                intServer.initialize(*params)
                
            self._status = Microkernel.INITIALIZED
    
    def start(self, *params):
        if self._status == Microkernel.INITIALIZED:
            for intServer in self._internalServers.values():
                intServer.start(*params)
            
            self._status = Microkernel.STARTED
    
    def stop(self):
        if self._status == Microkernel.STARTED:
            for intServer in self._internalServers.values():
                intServer.stop()
            
            self._status = Microkernel.STOPED
            
    def executeMecanism(self, internalServerName, serviceName, action, *params):
        internalServer = self._internalServers[internalServerName]
        return internalServer.executeService(serviceName, action, *params)
    
    def getStatus(self):
        return self._status
    
