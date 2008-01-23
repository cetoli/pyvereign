from atlas.api.env.hardware.service.AbstractHardwareService import AbstractHardwareService
from atlas.api.env.hardware.service.MachineService import MachineService

class AbstractMachineService(AbstractHardwareService, MachineService):
    
    def initialize(self, *params):
        AbstractHardwareService.initialize(self)
        self._machine = None
        self._name = "machine"
    
    def start(self, *params):
        if not self._dataSource:
            raise RuntimeError("Data source is none.")
        self._machine = self._dataSource.retrieveMachine()
    
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
    
    def getHardwareId(self):
        return self._machine.getHardwareId()
    
    def getDomain(self):
        return self._machine.getDomain()
    
    def getNumberOfProcessors(self):
        return self._machine.getNumberOfProcessors()
    
    def getTotalPhysicalMemory(self):
        return self._machine.getTotalPhysicalMemory()
    
    def getName(self):
        return self._name