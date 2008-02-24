class CommunicationService(object):
    
    NON_INITIALIZED = 0
    INITIALIZED = 1
    STARTED = 2
    STOPED = 3
    
    def __init__(self):
        raise NotImplementedError()
    
    def initialize(self, communication):
        pass
    
    def start(self, *params):
        pass
    
    def getName(self):
        pass
    
    def stop(self):
        pass
    
    def getStatus(self):
        pass