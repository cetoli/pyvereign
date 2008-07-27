from org.pyvereign.environment.instrumentation.hardware.battery import Battery
from org.pyvereign.environment.instrumentation.hardware.disk_drive import DiskDrive
from org.pyvereign.environment.instrumentation.hardware.machine import Machine
from org.pyvereign.environment.instrumentation.hardware.network_adapter import NetworkAdapter
from org.pyvereign.environment.instrumentation.hardware.physical_memory import PhysicalMemory
from org.pyvereign.environment.instrumentation.hardware.processor import Processor

class HardwareFactory(object):
    
    def __init__(self):
        raise NotImplementedError()
    
    @classmethod
    def createBattery(self):
        return Battery()
    
    @classmethod
    def createDiskDrive(self):
        return DiskDrive()
    
    @classmethod
    def createMachine(self):
        return Machine()
    
    @classmethod
    def createNetworkAdapter(self):
        return NetworkAdapter()
    
    @classmethod
    def createPhysicalMemory(self):
        return PhysicalMemory()
    
    @classmethod
    def createProcessor(self):
        return Processor()