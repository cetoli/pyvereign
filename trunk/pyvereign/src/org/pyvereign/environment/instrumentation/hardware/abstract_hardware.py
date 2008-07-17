from org.pyvereign.base.object import Object
from org.pyvereign.util.decorators.public import public
from org.pyvereign.util.decorators.return_type import return_type
from org.pyvereign.util.decorators.require import require

class AbstractHardware(Object):
    
    def __init__(self):
        raise NotImplementedError()
        
    @public
    @return_type(str)
    def getDescription(self):
        return self.__description
    
    @public
    @return_type(str)
    def getProduct(self):
        return self.__product
    
    @public
    @return_type(str)
    def getVendor(self):
        return self.__vendor
    
    @public
    @return_type(str)
    def getSerial(self):
        return self.__serial
    
    @public
    @return_type(str)
    def getLogicalName(self):
        return self.__logicalName
    
    @public
    @return_type(str)
    def getHardwareId(self):
        return self.__hardwareId
    
    @public
    @return_type(str)
    @require("description", str)
    def setDescription(self, description):
        self.__description = description
        return self.__description
    
    @public
    @return_type(str)
    @require("product", str)
    def setProduct(self, product):
        self.__product = product
        return self.__product
    
    @public
    @return_type(str)
    @require("vendor", str)
    def setVendor(self, vendor):
        self.__vendor = vendor
        return self.__vendor
    
    @public
    @return_type(str)
    @require("serial", str)
    def setSerial(self, serial):
        self.__serial = serial
        return self.__serial
    
    @public
    @return_type(str)
    @require("name", str)
    def setLogicalName(self, name):
        self.__logicalName = name
        return self.__logicalName
    
    @public
    @return_type(str)
    @require("hardwareId", str)
    def setHardwareId(self, hardwareId):
        self.__hardwareId = hardwareId
        return self.__hardwareId