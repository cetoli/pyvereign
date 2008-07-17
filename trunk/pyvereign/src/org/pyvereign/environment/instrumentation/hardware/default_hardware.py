from org.pyvereign.environment.instrumentation.hardware.abstract_hardware import AbstractHardware

class DefaultHardware(AbstractHardware):
    
    def __init__(self):
        self.setDescription("")
        self.setHardwareId("")
        self.setLogicalName("")
        self.setProduct("")
        self.setSerial("")
        self.setVendor("")