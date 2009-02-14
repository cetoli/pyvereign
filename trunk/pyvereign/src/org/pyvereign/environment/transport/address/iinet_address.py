from org.pyvereign.base.interface import Interface

class IInetAddress(object):
    
    __metaclass__ = Interface
    
    def __init__(self):
        raise NotImplementedError()
    
    def getFamily(self):
        pass
    
    def getIPAddress(self):
        pass
    
    def getPort(self):
        pass
    
    def getTuple(self):
        pass
    
    def isBroadcastAddress(self):
        pass
    
    def isBindAddress(self):
        pass
    
    def setPort(self, port):
        pass