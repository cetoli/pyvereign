class CommunicationAPIAdapter(object):
    
    def __init__(self):
        raise NotImplementedError()
    
    def supportBroadcasting(self, value):
        pass
    
    def reuseAddress(self, value):
        pass
    
    def open(self):
        pass

    def close(self):
        pass
    
    def setTimeOut(self, timeOut):
        pass
    
    def getTimeOut(self):
        pass
    
    def send(self, stream):
        pass
    
    def receive(self, bufferSize):
        pass
    
    def isSupportingBroadcasting(self):
        pass
    
    def isReusingAddress(self):
        pass
    
    def getInetAddress(self):
        pass
    
    def initialize(self):
        pass