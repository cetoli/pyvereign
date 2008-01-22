from atlas.api.env.hardware.DefaultMachine import DefaultMachine
import unittest

class DefaultMachineTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(DefaultMachine())
    
    def test_set_values_in_machine(self):
        machine = DefaultMachine()
        self.assertEquals("Computer", machine.setDescription("Computer"))
        self.assertEquals("HP Pavilion dv9502", machine.setProduct("HP Pavilion dv9502"))
        self.assertEquals("HP", machine.setVendor("HP"))
        self.assertEquals("abcd123", machine.setSerial("abcd123"))
        self.assertEquals("coverdale", machine.setLogicalName("coverdale"))
        self.assertEquals("123456", machine.setHardwareId("123456"))
        self.assertEquals("grupo", machine.setDomain("grupo"))
        self.assertEquals(2, machine.setNumberOfProcessors(2))
        self.assertEquals(2097152, machine.setTotalPhysicalMemory(2097152))
    
    def test_try_set_values_in_machine(self):
        machine = DefaultMachine()
        self.assertRaises(TypeError, machine.setDescription, 1)
        self.assertRaises(TypeError, machine.setDomain, 1)
        self.assertRaises(TypeError, machine.setHardwareId, 1)
        self.assertRaises(TypeError, machine.setLogicalName, 1)
        self.assertRaises(TypeError, machine.setNumberOfProcessors, "a")
        self.assertRaises(TypeError, machine.setTotalPhysicalMemory, "a")
        self.assertRaises(TypeError, machine.setProduct, 1)
        self.assertRaises(TypeError, machine.setSerial, 1)
        self.assertRaises(TypeError, machine.setVendor, 1)
    
    def test_try_set_none_values_in_machine(self):
        machine = DefaultMachine()
        self.assertRaises(RuntimeError, machine.setDescription, None)
        self.assertRaises(RuntimeError, machine.setDomain, None)
        self.assertRaises(RuntimeError, machine.setHardwareId, None)
        self.assertRaises(RuntimeError, machine.setLogicalName, None)
        self.assertRaises(RuntimeError, machine.setNumberOfProcessors, None)
        self.assertRaises(RuntimeError, machine.setTotalPhysicalMemory, None)
        self.assertRaises(RuntimeError, machine.setProduct, None)
        self.assertRaises(RuntimeError, machine.setSerial, None)
        self.assertRaises(RuntimeError, machine.setVendor, None)
        
    def test_get_values_in_machine(self):
        machine = DefaultMachine()
        self.assertEquals("Computer", machine.setDescription("Computer"))
        self.assertEquals("HP Pavilion dv9502", machine.setProduct("HP Pavilion dv9502"))
        self.assertEquals("HP", machine.setVendor("HP"))
        self.assertEquals("abcd123", machine.setSerial("abcd123"))
        self.assertEquals("coverdale", machine.setLogicalName("coverdale"))
        self.assertEquals("123456", machine.setHardwareId("123456"))
        self.assertEquals("grupo", machine.setDomain("grupo"))
        self.assertEquals(2, machine.setNumberOfProcessors(2))
        self.assertEquals(2097152, machine.setTotalPhysicalMemory(2097152))
        
        self.assertEquals("Computer", machine.getDescription())
        self.assertEquals("HP Pavilion dv9502", machine.getProduct())
        self.assertEquals("HP", machine.getVendor())
        self.assertEquals("abcd123", machine.getSerial())
        self.assertEquals("coverdale", machine.getLogicalName())
        self.assertEquals("123456", machine.getHardwareId())
        self.assertEquals("grupo", machine.getDomain())
        self.assertEquals(2, machine.getNumberOfProcessors())
        self.assertEquals(2097152, machine.getTotalPhysicalMemory())
    
