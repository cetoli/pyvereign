class Dispatcher(object):
    
    def __init__(self):
        raise NotImplementedError()
    
    def registerEventHandler(self, handler):
        pass
    
    def unregisterEventHandler(self, handler):
        pass
    
    def getNumberOfEventHandlers(self):
        pass
    
    def handleEvent(self, event):
        pass
    
    def initialize(self):
        pass
    
    
