class Receiver(object):
    
    def __init__(self):
        raise NotImplementedError()
    
    def initialize(self):
        pass
    
    def open(self):
        pass
    
    def bind(self):
        pass
    
    def close(self):
        pass
    
    def receive(self, bufferSize):
        pass
    
    def reuseAddress(self, flag):
        pass
    
    def isReusingAddress(self):
        pass
    
    def getInetAddress(self):
        pass
    
    def getProtocol(self):
        pass