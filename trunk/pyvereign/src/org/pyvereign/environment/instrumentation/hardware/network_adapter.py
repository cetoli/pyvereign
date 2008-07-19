from org.pyvereign.environment.instrumentation.hardware.default_hardware import DefaultHardware
from org.pyvereign.util.decorators.public import public
from org.pyvereign.util.decorators.return_type import return_type
from org.pyvereign.util.decorators.require import require

class NetworkAdapter(DefaultHardware):
    
    def __init__(self):
        DefaultHardware().__init__(self)
        self.setIPAddress("")
        self.setMACAddress("")
        self.setSpeed(0)
    
    @public
    @return_type(int)
    def getSpeed(self):
        return self.__speed
    
    @public
    @return_type(str)
    def getMACAddress(self):
        return self.__macaddress
    
    @public
    @return_type(str)
    def getIPAddress(self):
        return self.__ipaddress
    
    @public
    @return_type(int)
    @require("speed", int)
    def setSpeed(self, speed):
        self.__speed = speed
        return self.__speed
    
    @public
    @return_type(str)
    @require("macaddress", str)
    def setMACAddress(self, macaddress):
        self.__macaddress = macaddress
        return self.__macaddress
    
    @public
    @return_type(str)
    @require("ipaddress", str)
    def setIPAddress(self, ipaddress):
        self.__ipaddress = ipaddress
        return self.__ipaddress