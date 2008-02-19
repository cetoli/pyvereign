from threading import Thread

class StreamListener(Thread):
    
    def __init__(self, environment, receiver):
        Thread.__init__(self)
        self._receiver = receiver
        self._bufferSize = 1024
        self._environment = environment
        self._active = False
        self._transportListeners = {}
    
    def addTransportListener(self, uri, listener):
        self._transportListeners[uri] = listener
        return self._transportListeners[uri]
    
    def getNumberOfTransportListeners(self):
        return len(self._transportListeners)
    
    def setBufferSize(self, bufferSize):
        self._bufferSize = bufferSize
        
    def getBufferSize(self):
        return self._bufferSize
    
    def isActive(self):
        return self._active
    
    def open(self):
        try:
            return self._receiver.open()
        except:
            raise
    
    def run(self):
        try:
            self._active = self._receiver.bind()
            while True:
                stream = self._receiver.receive(self._bufferSize)
                if stream:
                    if stream == "STOP":
                        self._active = False
                
                if self._active == False:
                    "Shutdown"
                    return
                    
        except:
            raise
    
    
    def close(self):
        try:
            self._environment.executeService("transport", "sendStream", self._receiver.getProtocol().getName(), self._receiver.getInetAddress(), "STOP")
            return self._receiver.close()
        except:
            raise
    
    