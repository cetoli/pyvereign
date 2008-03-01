from atlas.api.com.ipc.handler.AbstractEventHandler import AbstractEventHandler
from threading import Thread

class DefaultEventHandler(AbstractEventHandler):
    
    def __init__(self):
        Thread.__init__(self)
        self.initialize()
        self._handle = "HANDLE"