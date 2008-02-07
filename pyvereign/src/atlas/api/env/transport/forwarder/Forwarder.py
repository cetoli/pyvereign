class Forwarder(object):
    
    def __init__(self):
        raise NotImplementedError()
    
    def open(self):
        pass
    
    def close(self):
        pass
    
    def send(self, stream):
        pass
    
    def supportBroadcasting(self, flag):
        pass
    
    def isSupportingBroadcasting(self):
        pass
    
    def getProtocol(self):
        pass
    
    def initialize(self):
        pass
    
    def getInetAddress(self):
        pass