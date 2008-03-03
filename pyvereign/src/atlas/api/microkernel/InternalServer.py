class InternalServer(object):
    
    NON_INITIALIZED = 0
    INITIALIZED = 1
    STARTED = 2
    STOPED = 3
    
    def __init__(self):
        raise NotImplementedError()
    
    def executeService(self, serviceName, action, *params):
        pass
    
    def initialize(self, *params):
        pass
    
    def start(self, *params):
        pass
    
    def stop(self):
        pass
    
    def registerService(self, name, service):
        pass
    
    def unregisterService(self, name):
        pass
    
    def clearServices(self):
        pass