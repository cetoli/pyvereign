from Queue import Queue
from atlas.api.com.endpoint.listener.EndpointListener import EndpointListener

class IncommingQueue(EndpointListener):
    
    def __init__(self, dispatcher):
        self._queue = Queue()
        self._dispatcher = dispatcher
        
    def enqueue(self, event):
        self._queue.put(event)
        return event
    
    def dequeue(self):
        return self._queue.get()
    
    def processMessage(self, message):
        pass
    
    