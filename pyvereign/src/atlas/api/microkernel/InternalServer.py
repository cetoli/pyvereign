class InternalServer(object):
    
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