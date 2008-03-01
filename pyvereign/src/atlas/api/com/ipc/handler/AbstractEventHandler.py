from atlas.api.com.ipc.handler.EventHandler import EventHandler
from threading import Thread
from copy import copy

class AbstractEventHandler(EventHandler, Thread):
    
    def __init__(self):
        raise NotImplementedError()
    
    def initialize(self):
        self._handle = ""
        self._event = None
        
    def handleEvent(self, event):
        self._event = event
        self.start()
        
    def clone(self):
        return copy(self)
    
    def getEvent(self):
        return self._event