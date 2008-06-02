from org.pyvereign.core.communication.ipc.dispatcher.EventDispatcher import EventDispatcher

class AbstractEventDispatcher(EventDispatcher):
    
    def init(self):
        self._eventHandlers = {}