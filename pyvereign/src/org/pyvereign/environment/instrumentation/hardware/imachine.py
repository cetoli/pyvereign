from org.pyvereign.environment.instrumentation.hardware.ihardware import IHardware
from org.pyvereign.base.interface import Interface

class IMachine(IHardware):
    
    __metaclass__ = Interface
    
    def __init__(self):
        raise NotImplementedError()
    
    def getDomain(self):
        raise NotImplementedError()
    
    def getNumberOfProcessors(self):
        raise NotImplementedError()
    
    def getTotalPhysicalMemory(self):
        raise NotImplementedError()
    
    def setDomain(self, domain):
        raise NotImplementedError()
    
    def setNumberOfProcessors(self, processors):
        raise NotImplementedError()
    
    def setTotalPhysicalMemory(self, memory):
        raise NotImplementedError()