from threading import Thread
from org.pyvereign.core.environment.transport.listener.TransportListener import TransportListener

class StreamListener(Thread):
    
    def __init__(self, receiver):
        Thread.__init__(self)
        self._receiver = receiver
        self._bufferSize = 1024
        self._active = False
        self._transportListeners = {}
        self._id = ""
    
    def addTransportListener(self, uri, listener):
        if not uri:
            raise RuntimeError("uri is none.")
        if not isinstance(uri, str):
            raise TypeError("uri is not an instance of str class.")
        if not listener:
            raise RuntimeError("listener is none.")
        if not isinstance(listener, TransportListener):
            raise TypeError("listener is not an instance of TransportListener class.")
        self._transportListeners[uri] = listener
        return self._transportListeners[uri]
    
    def removeTransportListener(self, uri):
        if not uri:
            raise RuntimeError("uri is none.")
        if not isinstance(uri, str):
            raise TypeError("uri is not an instance of str class.")
        listener = self._transportListeners[uri]
        del self._transportListeners[uri]
        return listener
    
    def getTransportListener(self, uri):
        if not uri:
            raise RuntimeError("uri is none.")
        if not isinstance(uri, str):
            raise TypeError("uri is not an instance of str class.")
        return self._transportListeners[uri]
    
    def getNumberOfTransportListeners(self):
        return len(self._transportListeners)
    
    def setBufferSize(self, bufferSize):
        if not bufferSize:
            raise RuntimeError("bufferSize is none.")
        if bufferSize <= 0:
            raise RuntimeError("negative or zero bufferSize")
        if not isinstance(bufferSize, int):
            raise TypeError("bufferSize is not an instance of int class.")
        self._bufferSize = bufferSize
        return self._bufferSize
        
    def getBufferSize(self):
        return self._bufferSize
    
    def isActive(self):
        return self._active
    
    def reuseAddress(self, flag):
        if flag == None:
            raise RuntimeError("flag is none.")
        if not isinstance(flag, bool):
            raise TypeError("flag is not an instance of bool class.")
        return self._receiver.reuseAddress(flag)
    
    def open(self, port):
        if not port:
            raise RuntimeError("port is none.")
        if port <= 0:
            raise RuntimeError("negative or zero port.")
        if not isinstance(port, int):
            raise TypeError("port is not an instance of int class.")
        try:
            self._receiver.getInetAddress().setPort(port)
            return self._receiver.open()
        except:
            raise
    
    def run(self):
        try:
            try:
                self._active = self._receiver.bind()
                while self._active:
                    stream = self._receiver.receive(self._bufferSize)
                    if stream:
                        if self._id == stream:
                            break
                        for listener in self._transportListeners.values():
                            listener.processStream(stream)
                print "passou"        
            except:
                raise
        finally:
            self._receiver.close()
    
    
    def close(self):
        return True
    
    