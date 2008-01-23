from atlas.api.env.hardware.DefaultNetworkController import DefaultNetworkController
import unittest

class DefaultNetworkControllerTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(DefaultNetworkController())
        
    def test_set_valid_values_in_network_controller(self):
        controller = DefaultNetworkController()
        self.assertEquals("Network Controller", controller.setDescription("Network Controller"))
        self.assertEquals("123456", controller.setHardwareId("123456"))
        self.assertEquals("192.168.1.2", controller.setIPAddress("192.168.1.2"))
        self.assertEquals("Conexao Local", controller.setLogicalName("Conexao Local"))
        self.assertEquals("aa:bb:cc", controller.setMACAddress("aa:bb:cc"))
        self.assertEquals(100, controller.setMaxSpeed(100))
        self.assertEquals("Ethernet Controller", controller.setProduct("Ethernet Controller"))
        self.assertEquals("aa:bb:cc", controller.setSerial("aa:bb:cc"))
        self.assertEquals(100, controller.setSpeed(100))
        self.assertEquals("NVidia", controller.setVendor("NVidia"))
    
    def test_try_set_invalid_values_in_network_controller(self):
        controller = DefaultNetworkController()
        self.assertRaises(TypeError, controller.setDescription, 1)
        self.assertRaises(TypeError, controller.setHardwareId, 1)
        self.assertRaises(TypeError, controller.setIPAddress, 1)
        self.assertRaises(TypeError, controller.setLogicalName, 1)
        self.assertRaises(TypeError, controller.setMACAddress, 1)
        self.assertRaises(TypeError, controller.setMaxSpeed, "a")
        self.assertRaises(TypeError, controller.setProduct, 1)
        self.assertRaises(TypeError, controller.setSerial, 1)
        self.assertRaises(TypeError, controller.setSpeed, "a")
        self.assertRaises(TypeError, controller.setVendor, 1)
    
    def test_try_set_none_values_in_network_controller(self):
        controller = DefaultNetworkController()
        self.assertRaises(RuntimeError, controller.setDescription, None)
        self.assertRaises(RuntimeError, controller.setHardwareId, None)
        self.assertRaises(RuntimeError, controller.setIPAddress, None)
        self.assertRaises(RuntimeError, controller.setLogicalName, None)
        self.assertRaises(RuntimeError, controller.setMACAddress, None)
        self.assertRaises(RuntimeError, controller.setMaxSpeed, None)
        self.assertRaises(RuntimeError, controller.setProduct, None)
        self.assertRaises(RuntimeError, controller.setSerial, None)
        self.assertRaises(RuntimeError, controller.setSpeed, None)
        self.assertRaises(RuntimeError, controller.setVendor, None)
        