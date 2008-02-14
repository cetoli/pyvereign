from threading import Thread

class StreamListener(Thread):
    
    def __init__(self, environment, receiver):
        Thread.__init__(self)
        self._receiver = receiver
        self._bufferSize = 1024
        self._environment = environment
        self._active = False
        self._streamListeners = {}
    
    def setBufferSize(self, bufferSize):
        self._bufferSize = bufferSize
        
    def addStreamLister(self, id, listener):
        self._streamListeners[id] = listener
        return self._streamListeners[id]
        
    def removeStreamListener(self, id):
        listener = self._streamListeners[id]
        del self._streamListeners[id]
        return listener
    
    def getStreamListener(self, id):
        return self._streamListeners[id]
    
    def getBufferSize(self):
        return self._bufferSize
    
    def isActive(self):
        return self._active
    
    def open(self):
        try:
            self._receiver.open()
        except:
            raise
    
    def run(self):
        try:
            self._active = self._receiver.bind()
            while self._active:
                stream = self._receiver.receive(self._bufferSize)
                if stream:
                    if stream == "STOP":
                        break
                    for l in self._streamListeners.values():
                        l.processStream(stream)
        except:
            raise
    
    
    def close(self):
        try:
            self._environment.executeService("transport", "sendStream", self._receiver.getProtocol().getName(), self._receiver.getInetAddress(), "STOP")
            self._receiver.close()
        except:
            raise
    
    