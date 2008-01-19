from atlas.api.env.hardware.Hardware import Hardware

class AbstractHardware(Hardware):
    """
    Define an abstract class for several types of hardware.
    
    @author: Fabricio
    @since: 19/01/2008 - 10:19:10
    @version: version
    """
    
    def initialize(self):
        self._description = ""
        self._product = ""
        self._vendor = ""
        self._serial = ""
        self._logicalName = ""
        self._id = ""
    
    def setDescription(self, description):
        self._description = description
        return self._description
    
    def getDescription(self):
        return self._description
    
    def setProduct(self, product):
        self._product = product
        return self._product
    
    def getProduct(self):
        return self._product
    
    def setVendor(self, vendor):
        self._vendor = vendor
        return self._vendor
    
    def setSerial(self, serial):
        self._serial = serial
        return self._serial
    
    def getSerial(self):
        return self._serial
    
    def setLogicalName(self, logicalName):
        self._logicalName = logicalName
        return self._logicalName
    
    def getLogicalName(self):
        return self._logicalName
    
    def getId(self):
        return self._id
    
    def setId(self, id):
        self._id = id
        return self._id
    