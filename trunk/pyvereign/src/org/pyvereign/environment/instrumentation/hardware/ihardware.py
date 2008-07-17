from org.pyvereign.base.interface import Interface

class IHardware(object):
    
    __metaclass__ = Interface
    
    def __init__(self):
        raise NotImplementedError()
    
    def getDescription(self):
        raise NotImplementedError()
    
    def getProduct(self):
        raise NotImplementedError()
    
    def getVendor(self):
        raise NotImplementedError()
    
    def getSerial(self):
        raise NotImplementedError()
    
    def getLogicalName(self):
        raise NotImplementedError()
    
    def getHardwareId(self):
        raise NotImplementedError()
    
    def setDescription(self, description):
        raise NotImplementedError()
    
    def setProduct(self, product):
        raise NotImplementedError()
    
    def setVendor(self, vendor):
        raise NotImplementedError()
    
    def setSerial(self, serial):
        raise NotImplementedError()
    
    def setLogicalName(self, name):
        raise NotImplementedError()
    
    def setHardwareId(self, hardwareId):
        raise NotImplementedError()