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
        if not description:
            raise RuntimeError("None parameter")
        if not isinstance(description, str):
            raise TypeError("Invalid data type.")
        self._description = description
        return self._description
    
    def getDescription(self):
        return self._description
    
    def setProduct(self, product):
        if not product:
            raise RuntimeError("None parameter")
        if not isinstance(product, str):
            raise TypeError("Invalid data type.")
        self._product = product
        return self._product
    
    def getProduct(self):
        return self._product
    
    def setVendor(self, vendor):
        if not vendor:
            raise RuntimeError("None parameter")
        if not isinstance(vendor, str):
            raise TypeError("Invalid data type.")
        self._vendor = vendor
        return self._vendor
    
    def setSerial(self, serial):
        if not serial:
            raise RuntimeError("None parameter")
        if not isinstance(serial, str):
            raise TypeError("Invalid data type.")
        self._serial = serial
        return self._serial
    
    def getSerial(self):
        return self._serial
    
    def setLogicalName(self, logicalName):
        if not logicalName:
            raise RuntimeError("None parameter")
        if not isinstance(logicalName, str):
            raise TypeError("Invalid data type.")
        self._logicalName = logicalName
        return self._logicalName
    
    def getLogicalName(self):
        return self._logicalName
    
    def getHardwareId(self):
        return self._id
    
    def setHardwareId(self, id):
        if not id:
            raise RuntimeError("None parameter")
        if not isinstance(id, str):
            raise TypeError("Invalid data type.")
        self._id = id
        return self._id
    
    def getVendor(self):
        return self._vendor
    