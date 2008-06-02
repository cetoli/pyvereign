from org.pyvereign.core.communication.ipc.event.AbstractEvent import AbstractEvent

class EventImpl(AbstractEvent):
    
    def __init__(self, handle, origin, destination):
        self.init(handle, origin, destination)