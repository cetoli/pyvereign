from org.pyvereign.core.environment.instrumentation.dto.system.SystemElement import SystemElement

class Process(SystemElement):
    """
    Defines the common interface for objects that represent SO processes. 
    
    @author: Fabricio
    @since: 28/03/2008 - 13:40:01
    @version: 0.0.1
    """
    
    def __init__(self):
        raise NotImplementedError()
    
    def getProcessId(self):
        """
        Gets the identifier of process.
        @return: Returns the identifier of process.
        @rtype: str
        """
        pass
    
    def getMaximumWorkingSetSize(self):
        """
        Gets the maximum working set size the process
        @return: Returns the maximum working set size the process
        @rtype: int
        """
        pass
    
    def getMinimumWorkingSetSize(self):
        """
        Gets the minimum working set size of process.
        @return: Returns the minimum working set size of process.
        @rtype: int
        """
        pass
    
    def getVirtualSize(self):
        """
        Gets the virtual size of process.
        @return: Returns the virtual size of process.
        @rtype: int
        """
        pass