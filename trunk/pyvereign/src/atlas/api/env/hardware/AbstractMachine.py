from atlas.api.env.hardware.AbstractHardware import AbstractHardware
from atlas.api.env.hardware.Machine import Machine

class AbstractMachine(AbstractHardware, Machine):
    
    def initialize(self):
        AbstractHardware.initialize(self)
        self._domain = ""
        self._numberOfProcessors = 0
        self._totalPhysicalMemory = 0

    def setDomain(self, domain):
        if not domain:
            raise RuntimeError("None parameter")
        if not isinstance(domain, str):
            raise TypeError("Invalid data type.")
        self._domain = domain
        return self._domain
    
    def getDomain(self):
        return self._domain
    
    def setNumberOfProcessors(self, processors):
        if not processors:
            raise RuntimeError("None parameter")
        if not isinstance(processors, int):
            raise TypeError("Invalid data type.")
        if processors < 1:
            raise RuntimeError("Invalid value.")
        self._numberOfProcessors = processors
        return self._numberOfProcessors
    
    def getNumberOfProcessors(self):
        return self._numberOfProcessors
    
    def setTotalPhysicalMemory(self, memory):
        if not memory:
            raise RuntimeError("None parameter")
        if not isinstance(memory, int):
            raise TypeError("Invalid data type.")
        if memory < 1:
            raise RuntimeError("Invalid value.")
        self._totalPhysicalMemory = memory
        return self._totalPhysicalMemory
    
    def getTotalPhysicalMemory(self):
        return self._totalPhysicalMemory