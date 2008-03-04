from atlas.api.com.ipc.event.AbstractEvent import AbstractEvent

class DefaultEvent(AbstractEvent):
    
    def __init__(self, handle, origin, destination):
        self.initialize()
        self._handle = handle
        self._origin = origin
        self._destination = destination