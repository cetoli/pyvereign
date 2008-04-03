from org.pyvereign.core.environment.instrumentation.dto.hardware.Hardware import Hardware

class PhysicalMemory(Hardware):
    """
    Defines the common interface for physical memories.
    
    @author: Fabricio
    @since: 21/03/2008 - 23:22:24
    @version: 0.0.1
    """
    
    def getCapacity(self):
        """
        Gets the capacity of memory.
        @return: Returns the capacity of memory.
        @rtype: str
        """
        pass
    
    def getDataWidth(self):
        """
        Gets the data with of memory.
        @return: Returns the data with of memory.
        @rtype: int
        """
        pass
    
    def getSpeed(self):
        """
        Gets the speed of memory.
        @return: Returns the speed of memory.
        @rtype: int
        """
        pass
    
    def getDeviceLocator(self):
        """
        Gets the device locator of memory.
        @return: Returns the device locator of memory.
        @rtype: str
        """
        pass