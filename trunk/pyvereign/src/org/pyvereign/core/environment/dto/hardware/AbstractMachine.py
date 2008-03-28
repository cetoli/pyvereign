from org.pyvereign.core.environment.dto.hardware.AbstractHardware import AbstractHardware
from org.pyvereign.core.environment.dto.hardware.Machine import Machine

class AbstractMachine(AbstractHardware, Machine):
    """
    description
    
    @author: Fabricio
    @since: 22/03/2008 - 01:52:43
    @version: version
    """
    
    def init(self, values):
        self._domain = ""
        """
        @ivar: the domain of machine user.
        @type: str
        """
        self._processors = 0
        """
        @ivar: the processor number of machine user.
        @type: int
        """
        self._totalMemory = 0
        """
        @ivar: the total physical memory of machine user.
        @type: int
        """
        AbstractHardware.init(self, values)
        
        if values.has_key("domain"):
            self._domain = values["domain"]
        if values.has_key("processors"):
            self._processors = values["processors"]
        if values.has_key("totalMemory"):
            self._totalMemory = values["totalMemory"]
    
    def getDomain(self):
        return self._domain
    
    def getNumberOfProcessors(self):
        return self._processors
    
    def getTotalPhysicalMemory(self):
        return self._totalMemory
        
    