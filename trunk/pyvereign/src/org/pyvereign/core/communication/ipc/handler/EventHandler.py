from threading import Thread

class EventHandler(Thread):
    
    def __init__(self):
        raise NotImplementedError()
    
    def getHandle(self):
        pass
    
    def handleEvent(self, event):
        pass