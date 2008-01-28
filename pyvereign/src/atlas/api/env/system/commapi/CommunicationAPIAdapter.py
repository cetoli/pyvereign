class CommunicationAPIAdapter(object):
    
    def __init__(self):
        raise NotImplementedError()
    
    def initialize(self):
        pass
    
    def open(self):
        pass
    
    def close(self):
        pass
    
    def send(self, stream):
        pass
    
    def receive(self, bufferSize):
        pass
    
    def sendTo(self, address, stream):
        pass
    
    def receiveFrom(self, bufferSize):
        pass
    
    def setTimeOut(self, timeOut):
        pass
    
    def getTimeOut(self):
        pass
    
    def getProtocolName(self):
        pass