from threading import Thread
from atlas.api.com.ipc.handler.EventHandler import EventHandler

class AbstractEventHandler(Thread, EventHandler):
    
    def __init__(self):
        raise NotImplementedError()
    
    def initialize(self):
        self._event = None
    
    def handleEvent(self, event):
        self._event = event
        self.start()
        
