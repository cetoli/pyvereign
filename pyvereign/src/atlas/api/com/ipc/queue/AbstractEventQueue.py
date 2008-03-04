from atlas.api.com.ipc.queue.EventQueue import EventQueue
from Queue import Queue
from atlas.api.com.ipc.event.Event import Event
from atlas.api.com.endpoint.message.EndpointMessage import EndpointMessage

class AbstractEventQueue(EventQueue):
    
    def initialize(self):
        self._queue = Queue()
        
    def enqueue(self, event):
        if not event:
            raise RuntimeError("event is none.")
        if not isinstance(event, Event):
            raise TypeError("event is not an instance of Event class.")
        self._queue.put(event)
        return event
    
    def dequeue(self):
        return self._queue.get()
    
    def getSize(self):
        return self._queue.qsize()
    
    def processMessage(self, message):
        if not message:
            raise RuntimeError("message is none.")
        if not isinstance(message, EndpointMessage):
            raise TypeError("message is not an instance of EndpointMessage class.")
        event = message.getEvent()
        self.enqueue(event)
        