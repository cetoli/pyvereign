from org.pyvereign.core.environment.dto.hardware.PhysicalMemory import PhysicalMemory
from org.pyvereign.core.environment.dto.hardware.AbstractHardware import AbstractHardware

class AbstractPhysicalMemory(PhysicalMemory, AbstractHardware):
    
    def init(self, values):
        self._capacity = 0
        self._dataWidth =0
        self._speed = 0
        self._deviceLocator = ""
        AbstractHardware.init(self, values)
        
        if values.has_key("capacity"):
            self._capacity = values["capacity"]
        
        if values.has_key("dataWidth"):
            self._dataWidth = values["dataWidth"]
        
        if values.has_key("speed"):
            self._speed = values["speed"]
            
        if values.has_key("deviceLocator"):
            self._deviceLocator = values["deviceLocator"]
    
    def getCapacity(self):
        """
        Gets the capacity of memory.
        @return: Returns the capacity of memory.
        @rtype: str
        """
        return self._capacity
    
    def getDataWidth(self):
        """
        Gets the data with of memory.
        @return: Returns the data with of memory.
        @rtype: int
        """
        return self._dataWidth
    
    def getSpeed(self):
        """
        Gets the speed of memory.
        @return: Returns the speed of memory.
        @rtype: int
        """
        return self._speed
    
    def getDeviceLocator(self):
        """
        Gets the device locator of memory.
        @return: Returns the device locator of memory.
        @rtype: str
        """
        return self._deviceLocator
            
            