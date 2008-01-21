from atlas.api.env.service.AbstractHardwareService import AbstractHardwareService
from atlas.api.env.service.MachineService import MachineService

class AbstractMachineService(AbstractHardwareService, MachineService):
    
    def initialize(self, *params):
        AbstractHardwareService.initialize(self)
        self._machine = None
    
    def getDescription(self):
        return self._machine.getDescription()
    
    def getProduct(self):
        return self._machine.getProduct()
    
    def getVendor(self):
        return self._machine.getVendor()
    
    def getSerial(self):
        return self._machine.getSerial()
    
    def getLogicalName(self):
        return self._machine.getLogicalName()
    
    def setId(self, id):
        return self._machine.getId()
    
    def getDomain(self):
        return self._machine.getDomain()
    
    def getNumberOfProcessors(self):
        return self._machine.getNumberOfProcessors()
    
    def getTotalPhysicalMemory(self):
        return self._machine.getTotalPhysicalMemory()