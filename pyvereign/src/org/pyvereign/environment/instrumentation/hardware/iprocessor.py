from org.pyvereign.base.interface import Interface

class IProcessor(object):
    
       
    __metaclass__ = Interface
    
    def __init__(self):
        raise NotImplementedError()
        
    def getArchitecture(self):
        raise NotImplementedError()
    
    def getCPUStatus(self):
        raise NotImplementedError()
    
    def getCurrentClockSpeed(self):
        raise NotImplementedError()
    
    def getL2CacheSize(self):
        raise NotImplementedError()
    
    def getL2CacheSpeed(self):
        raise NotImplementedError()
    
    def getLoadPercentage(self):
        raise NotImplementedError()
    
    def getMaxClockSpeed(self):
        raise NotImplementedError()
    
    def getProcessorId(self):
        raise NotImplementedError()
    
    def getProcessorType(self):
        raise NotImplementedError()
    
    def setArchitecture(self, architecture):
        raise NotImplementedError()
    
    def setCPUStatus(self, cpuStatus):
        raise NotImplementedError()
    
    def setCurrentClockSpeed(self, speed):
        raise NotImplementedError()
    
    def setL2CacheSize(self, l2CacheSize):
        raise NotImplementedError()
    
    def setL2CacheSpeed(self, l2CacheSpeed):
        raise NotImplementedError()
    
    def setLoadPercentage(self, loadPercentage):
        raise NotImplementedError()
    
    def setMaxClockSpeed(self, maxClockSpeed):
        raise NotImplementedError()
    
    def setProcessorId(self, processorId):
        raise NotImplementedError()
    
    def setProcessorType(self, processorType):
        raise NotImplementedError()
    
    