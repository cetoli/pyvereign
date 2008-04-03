from org.pyvereign.core.environment.instrumentation.dto.hardware.PhysicalMemoryImpl import PhysicalMemoryImpl
import unittest

class PhysicalMemoryImplTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(PhysicalMemoryImpl({}))
        
        values = {"capacity": 1024, "dataWidth": 64, "description": "Physical Memory",
                  "deviceLocator": "Memory", "hardwareId": "123", 
                  "logicalName": "Physical Memory", "product": "Physical Memory",
                  "serial": "123", "speed": 533, "vendor": "Teste"}
        physicalMemory = PhysicalMemoryImpl(values)
        self.assertEquals(1024, physicalMemory.getCapacity())
        self.assertEquals(64, physicalMemory.getDataWidth())
        self.assertEquals("Physical Memory", physicalMemory.getDescription())
        self.assertEquals("Memory", physicalMemory.getDeviceLocator())
        self.assertEquals("123", physicalMemory.getHardwareId())
        self.assertEquals("Physical Memory", physicalMemory.getLogicalName())
        self.assertEquals("Physical Memory", physicalMemory.getProduct())
        self.assertEquals("123", physicalMemory.getSerial())
        self.assertEquals(533, physicalMemory.getSpeed())
        self.assertEquals("Teste", physicalMemory.getVendor())
    
    def test_try_create_instance(self):
        self.assertRaises(RuntimeError, PhysicalMemoryImpl, {"test": "teste"})