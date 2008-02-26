class Event(object):
    
    def __init__(self, handle, origin, destination):
        self._handle = handle
        self._origin = origin
        self._destination = destination
    
    def getHandle(self):
        return self._handle
    
    def getOrigin(self):
        return self._origin
    
    def getDestination(self):
        return self._destination
    
    