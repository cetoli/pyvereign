from atlas.api.com.ipc.event.Event import Event

class AbstractEvent(Event):
    
    def initialize(self):
        self._handle = ""
        self._origin = ""
        self._destination = ""
        
    def getHandle(self):
        return self._handle
    
    def getOrigin(self):
        return self._origin
    
    def getDestination(self):
        return self._destination