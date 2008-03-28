from org.pyvereign.core.environment.dto.hardware.AbstractPhysicalMemory import AbstractPhysicalMemory

class PhysicalMemoryImpl(AbstractPhysicalMemory):
    
    def __init__(self, values):
        self.init(values)