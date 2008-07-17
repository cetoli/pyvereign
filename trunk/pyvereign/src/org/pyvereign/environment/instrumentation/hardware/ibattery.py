from org.pyvereign.environment.instrumentation.hardware.ihardware import IHardware
from org.pyvereign.base.interface import Interface

class IBattery(IHardware):
    
    __metaclass__ = Interface
    
    def __init__(self):
        raise NotImplementedError()
    
    def getEstimatedChargeRemaining(self):
        raise NotImplementedError()
    
    def setEstimatedChargeRemaining(self, charge):
        raise NotImplementedError()