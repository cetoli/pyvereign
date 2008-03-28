from org.pyvereign.core.environment.dto.hardware.MachineImpl import MachineImpl
import unittest

class MachineImplTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(MachineImpl({}))
        
        values = {"description": "a", "domain":"grupo", "hardwareId":"123", 
                  "logicalName": "coverdale", "processors": 2, "product": "laptop",
                  "serial": "abc123", "totalMemory": 2048, "vendor": "HP"}
        machine = MachineImpl(values)
        self.assertEquals("a", machine.getDescription())
        self.assertEquals("grupo", machine.getDomain())
        self.assertEquals("123", machine.getHardwareId())
        self.assertEquals("coverdale", machine.getLogicalName())
        self.assertEquals(2, machine.getNumberOfProcessors())
        self.assertEquals("laptop", machine.getProduct())
        self.assertEquals("abc123", machine.getSerial())
        self.assertEquals(2048, machine.getTotalPhysicalMemory())
        self.assertEquals("HP", machine.getVendor())
    
    def test_try_create_instance(self):
        self.assertRaises(RuntimeError, MachineImpl, {"test": "test"})
    