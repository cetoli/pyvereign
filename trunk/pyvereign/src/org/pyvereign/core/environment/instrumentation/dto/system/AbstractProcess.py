from org.pyvereign.core.environment.instrumentation.dto.system.Process import Process
from org.pyvereign.core.environment.instrumentation.dto.system.AbstractSystemElement import AbstractSystemElement

class AbstractProcess(Process, AbstractSystemElement):
    """
    Defines the common implementation of Process interface. 
    
    @author: Fabricio
    @since: 28/03/2008 - 14:04:05
    @version: 0.0.1
    """
    
    def init(self, values):
        self._processId = ""
        """
        @ivar: the identifier of process.
        @type: str
        """
        self._maximumWorkingSetSize = 0
        """
        @ivar: the maximum working size of process.
        @type: int
        """
        self._minimumWorkingSetSize = 0
        """
        @ivar: the minimum working size of process.
        @type: int
        """
        self._virtualSize = 0
        """
        @ivar: the virtual size of process.
        @type: int
        """
        AbstractSystemElement.init(self, values)
        
        if values.has_key("processId"):
            self._processId = values["processId"]
        
        if values.has_key("maximumWorkingSetSize"):
            self._maximumWorkingSetSize = values["maximumWorkingSetSize"]
        
        if values.has_key("minimumWorkingSetSize"):
            self._minimumWorkingSetSize = values["minimumWorkingSetSize"]
        
        if values.has_key("virtualSize"):
            self._virtualSize = values["virtualSize"]
    
    def getProcessId(self):
        """
        Gets the identifier of process.
        @return: Returns the identifier of process.
        @rtype: str
        """
        return self._processId
    
    def getMaximumWorkingSetSize(self):
        """
        Gets the maximum working set size the process
        @return: Returns the maximum working set size the process
        @rtype: int
        """
        return self._maximumWorkingSetSize
    
    def getMinimumWorkingSetSize(self):
        """
        Gets the minimum working set size of process.
        @return: Returns the minimum working set size of process.
        @rtype: int
        """
        return self._minimumWorkingSetSize
    
    def getVirtualSize(self):
        """
        Gets the virtual size of process.
        @return: Returns the virtual size of process.
        @rtype: int
        """
        return self._virtualSize