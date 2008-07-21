from org.pyvereign.base.interface import Interface

class IPhysicalMemory(object):
    
    __metaclass__ = Interface
    
    def __init__(self):
        raise NotImplementedError()
    
    def getCapacity(self):
        raise NotImplementedError()
    
    def getDataWidth(self):
        raise NotImplementedError()
    
    def getSpeed(self):
        raise NotImplementedError()
    
    def setCapacity(self, capacity):
        raise NotImplementedError()
    
    def setDataWidth(self, dataWidth):
        raise NotImplementedError()
    
    def setSpeed(self, speed):
        raise NotImplementedError()