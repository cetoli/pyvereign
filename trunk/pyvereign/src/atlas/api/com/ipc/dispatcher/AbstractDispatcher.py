from atlas.api.com.ipc.dispatcher.Dispatcher import Dispatcher

class AbstractDispatcher(Dispatcher):
    
    def initialize(self):
        self._handlers = {}
        
    def registerEventHandler(self, handler):
        self._handlers[handler.getHandle()] = handler
        return self._handlers[handler.getHandle()]
    
    def unregisterEventHandler(self, handle):
        h = self._handlers[handle]
        del self._handlers[handle]
        return h
    
    def getNumberOfEventHandlers(self):
        return len(self._handlers)
    
    def handleEvent(self, event):
        if not self._handlers[event.getHandle()]:
            return
        handler = self._handlers[event.getHandle()]
        clone = handler.clone()
        clone.handleEvent(event)
        return clone
    