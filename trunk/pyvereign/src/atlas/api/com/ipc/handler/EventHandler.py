class EventHandler(object):
    
    def __init__(self):
        raise NotImplementedError()
    
    def getHandle(self):
        pass
    
    def handleEvent(self, event):
        pass
    
    def initialize(self):
        pass
    
    def clone(self):
        pass
    
    def getEvent(self):
        pass