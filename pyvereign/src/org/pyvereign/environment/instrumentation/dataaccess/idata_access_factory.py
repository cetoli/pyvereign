from org.pyvereign.base.interface import Interface

class IDataAccessFactory(object):
    
    __metaclass__ = Interface
    
    def __init__(self):
        raise NotImplementedError()
    
    def createBatteryDAO(self):
        raise NotImplementedError()
    
    def createDiskDriveDAO(self):
        raise NotImplementedError()
    
    def createMachineDAO(self):
        raise NotImplementedError()
    
    def createNetworkAdapterDAO(self):
        raise NotImplementedError()
    
    def createPhysicalMemoryDAO(self):
        raise NotImplementedError()
    
    def createProcessorDAO(self):
        raise NotImplementedError()