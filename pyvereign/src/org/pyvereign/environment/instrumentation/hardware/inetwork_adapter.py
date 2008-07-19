from org.pyvereign.base.interface import Interface

class INetworkAdapter(object):
    
    __metaclass__ = Interface
    
    def __init__(self):
        raise NotImplementedError()
    
    def getSpeed(self):
        raise NotImplementedError()
    
    def getMACAddress(self):
        raise NotImplementedError()
    
    def getIPAddress(self):
        raise NotImplementedError()
    
    def setSpeed(self, speed):
        raise NotImplementedError()
    
    def setMACAddress(self, macaddress):
        raise NotImplementedError()
    
    def setIPAddress(self, ipaddress):
        raise NotImplementedError()