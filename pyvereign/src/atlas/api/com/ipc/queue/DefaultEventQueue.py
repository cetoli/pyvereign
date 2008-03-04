from atlas.api.com.ipc.queue.AbstractEventQueue import AbstractEventQueue

class DefaultEventQueue(AbstractEventQueue):
    
    def __init__(self):
        self.initialize()