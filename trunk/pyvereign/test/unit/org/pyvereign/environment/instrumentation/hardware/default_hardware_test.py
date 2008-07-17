from org.pyvereign.environment.instrumentation.hardware.default_hardware import DefaultHardware
import unittest

class DefaultHardwareTest(unittest.TestCase):
    
    def setUp(self):
        self.hardware = DefaultHardware()
    
    def test_create_instance(self):
        self.assertTrue(DefaultHardware())
        hardware = DefaultHardware()
        self.assertEquals("", hardware.getDescription())
        self.assertEquals("", hardware.getHardwareId())
        self.assertEquals("", hardware.getLogicalName())
        self.assertEquals("", hardware.getProduct())
        self.assertEquals("", hardware.getSerial())
        self.assertEquals("", hardware.getVendor())
    
    def test_set_get_description(self):
        self.assertEquals("Battery", self.hardware.setDescription("Battery"))
        self.assertEquals("Battery", self.hardware.getDescription())
        
        self.assertRaises(TypeError, self.hardware.setDescription, 1)
        self.assertRaises(TypeError, self.hardware.setDescription, False)
        self.assertRaises(TypeError, self.hardware.setDescription, True)
        self.assertRaises(TypeError, self.hardware.setDescription, 0.001)
        
    def test_set_get_hardware_id(self):
        self.assertEquals("123abd", self.hardware.setHardwareId("123abd"))
        self.assertEquals("123abd", self.hardware.getHardwareId())
        
        self.assertRaises(TypeError, self.hardware.setHardwareId, 1)
        self.assertRaises(TypeError, self.hardware.setHardwareId, False)
        self.assertRaises(TypeError, self.hardware.setHardwareId, True)
        self.assertRaises(TypeError, self.hardware.setHardwareId, 0.001)
        
    def test_set_get_logical_name(self):
        self.assertEquals("battery", self.hardware.setLogicalName("battery"))
        self.assertEquals("battery", self.hardware.getLogicalName())
        
        self.assertRaises(TypeError, self.hardware.setLogicalName, 1)
        self.assertRaises(TypeError, self.hardware.setLogicalName, False)
        self.assertRaises(TypeError, self.hardware.setLogicalName, True)
        self.assertRaises(TypeError, self.hardware.setLogicalName, 0.001)
        
    def test_set_get_product(self):
        self.assertEquals("hardware", self.hardware.setProduct("hardware"))
        self.assertEquals("hardware", self.hardware.getProduct())
        
        self.assertRaises(TypeError, self.hardware.setProduct, 1)
        self.assertRaises(TypeError, self.hardware.setProduct, False)
        self.assertRaises(TypeError, self.hardware.setProduct, True)
        self.assertRaises(TypeError, self.hardware.setProduct, 0.001)
    
    def test_set_get_serial(self):
        self.assertEquals("123456", self.hardware.setSerial("123456"))
        self.assertEquals("123456", self.hardware.getSerial())
        
        self.assertRaises(TypeError, self.hardware.setSerial, 1)
        self.assertRaises(TypeError, self.hardware.setSerial, False)
        self.assertRaises(TypeError, self.hardware.setSerial, True)
        self.assertRaises(TypeError, self.hardware.setSerial, 0.001)
        
    def test_set_get_vendor(self):
        self.assertEquals("hardware", self.hardware.setVendor("hardware"))
        self.assertEquals("hardware", self.hardware.getVendor())
        
        self.assertRaises(TypeError, self.hardware.setVendor, 1)
        self.assertRaises(TypeError, self.hardware.setVendor, False)
        self.assertRaises(TypeError, self.hardware.setVendor, True)
        self.assertRaises(TypeError, self.hardware.setVendor, 0.001)
        