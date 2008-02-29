class Dispatcher(object):
    
    def __init__(self):
        raise NotImplementedError()
    
    def registerEventHandler(self, handle, handler):
        pass
    
    def unregisterEventHandler(self, handle):
        pass
    
    def getNumberOfEventHandlers(self):
        pass
    
    def handleEvent(self, event):
        pass
    
    def initialize(self):
        pass