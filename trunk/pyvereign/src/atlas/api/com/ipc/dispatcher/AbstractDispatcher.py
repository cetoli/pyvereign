from atlas.api.com.ipc.dispatcher.Dispatcher import Dispatcher
from atlas.api.com.ipc.handler.EventHandler import EventHandler
from atlas.api.com.ipc.event.Event import Event

class AbstractDispatcher(Dispatcher):
    
    def initialize(self):
        self._handlers = {}
    
    def registerEventHandler(self, handle, handler):
        if not handle:
            raise RuntimeError("handle is none.")
        if not isinstance(handle, str):
            raise TypeError("handle is not an instance of str class.")
        if not handler:
            raise RuntimeError("handler is none.")
        if not isinstance(handler, EventHandler):
            raise TypeError("handler is not an instance of EventHandler class.")
        self._handlers[handle] = handler
        return self._handlers[handle]
    
    def getNumberOfEventHandlers(self):
        return len(self._handlers)
    
    def unregisterEventHandler(self, handle):
        if not handle:
            raise RuntimeError("handle is none.")
        if not isinstance(handle, str):
            raise TypeError("handle is not an instance of str class.")
        handler = self._handlers[handle]
        del self._handlers[handle]
        return handler
            
    def handleEvent(self, event):
        if not event:
            raise RuntimeError("event is none.")
        if not isinstance(event, Event):
            raise TypeError("event is not an instance of Event class.")
        if not self._handlers.has_key(event.getHandle()):
            return
        handler = self._handlers[event.getHandle()].clone()
        handler.handleEvent(event)
        return handler
