from threading import Thread
from random import random
from atlas.api.exception.TransportError import TransportError

class StreamListener(Thread):
    
    def __init__(self, environment, receiver):
        Thread.__init__(self)
        self._receiver = receiver
        self._bufferSize = 1024
        self._environment = environment
        self._active = False
        self._transportListeners = {}
        self._id = ""
    
    def addTransportListener(self, uri, listener):
        self._transportListeners[uri] = listener
        return self._transportListeners[uri]
    
    def removeTransportListener(self, uri):
        listener = self._transportListeners[uri]
        del self._transportListeners[uri]
        return listener
    
    def getTransportListener(self, uri):
        return self._transportListeners[uri]
    
    def getNumberOfTransportListeners(self):
        return len(self._transportListeners)
    
    def setBufferSize(self, bufferSize):
        self._bufferSize = bufferSize
        
    def getBufferSize(self):
        return self._bufferSize
    
    def isActive(self):
        return self._active
    
    def reuseAddress(self, flag):
        return self._receiver.reuseAddress(flag)
    
    def open(self, port):
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
        try:
            print self._receiver.getInetAddress().getTuple()
            self._id = str(random())
            self._environment.executeService("transport", "sendStream", self._receiver.getProtocol().getName(), self._receiver.getInetAddress(), str(self._id))
            return self._receiver.close()
        except TransportError, e:
            raise
    
    