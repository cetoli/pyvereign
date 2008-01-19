from atlas.api.env.hardware.AbstractHardware import AbstractHardware
from atlas.api.env.hardware.Machine import Machine

class AbstractMachine(AbstractHardware, Machine):
    
    def initialize(self):
        AbstractHardware.initialize(self)
        self._domain = ""
        self._numberOfProcessors = 0
        self._totalPhysicalMemory = 0

    def setDomain(self, domain):
        self._domain = domain
        return self._domain
    
    def getDomain(self):
        return self._domain
    
    def setNumberOfProcessors(self, processors):
        self._numberOfProcessors = processors
        return self._numberOfProcessors
    
    def getNumberOfProcessors(self):
        return self._numberOfProcessors
    
    def setTotalPhysicalMemory(self, memory):
        self._totalPhysicalMemory = memory
        return self._totalPhysicalMemory
    
    def getTotalPhysicalMemory(self):
        return self._totalPhysicalMemory