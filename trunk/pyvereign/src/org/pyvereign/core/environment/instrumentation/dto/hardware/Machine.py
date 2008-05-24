from org.pyvereign.core.environment.instrumentation.dto.hardware.Hardware import Hardware

class Machine(Hardware):
    """
    Defines 
    
    @author: Fabricio
    @since: 22/03/2008 - 01:47:30
    @version: 0.0.1
    """
    
    def getDomain(self):
        """
        Gets the domain of user machine.
        @return: Returns the domain of user machine.
        @rtype: str
        """
        pass
    
    def getNumberOfProcessors(self):
        """
        Gets the machine number of processors.
        @return: Returns the machine number of processors.
        @rtype: int
        """
        pass
    
    def getTotalPhysicalMemory(self):
        """
        Gets the total of physical memory.
        @return: Returns the total of physical memory.
        @rtype: int
        """
        pass
    