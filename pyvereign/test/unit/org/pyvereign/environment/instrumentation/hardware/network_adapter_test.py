from org.pyvereign.environment.instrumentation.hardware.network_adapter import NetworkAdapter
from org.pyvereign.error.illegal_argument_error import IllegalArgumentError
import unittest

class NetworkAdapterTest(unittest.TestCase):
    
    def setUp(self):
        self.adapter = NetworkAdapter()
    
    def test_create_instance(self):
        self.assertTrue(NetworkAdapter())
        adapter = NetworkAdapter()
        self.assertEquals("", adapter.getIPAddress())
        self.assertEquals("", adapter.getMACAddress())
        self.assertEquals(0, adapter.getSpeed())
        
    def test_set_get_ipaddress(self):
        self.assertEquals("127.0.0.1", self.adapter.setIPAddress("127.0.0.1"))
        self.assertEquals("127.0.0.1", self.adapter.getIPAddress())
        
        self.assertRaises(TypeError, self.adapter.setIPAddress, 123)
        self.assertRaises(TypeError, self.adapter.setIPAddress, True)
        self.assertRaises(TypeError, self.adapter.setIPAddress, False)
        self.assertRaises(TypeError, self.adapter.setIPAddress, 0.25)
        self.assertRaises(TypeError, self.adapter.setIPAddress, None)
        
    def test_set_get_mac_address(self):
        self.assertEquals("127.0.0.1", self.adapter.setMACAddress("127.0.0.1"))
        self.assertEquals("127.0.0.1", self.adapter.getMACAddress())
        
        self.assertRaises(TypeError, self.adapter.setMACAddress, 123)
        self.assertRaises(TypeError, self.adapter.setMACAddress, True)
        self.assertRaises(TypeError, self.adapter.setMACAddress, False)
        self.assertRaises(TypeError, self.adapter.setMACAddress, 0.25)
        self.assertRaises(TypeError, self.adapter.setMACAddress, None)
    
    def test_set_get_speed(self):
        self.assertEquals(100, self.adapter.setSpeed(100))
        self.assertEquals(100, self.adapter.getSpeed())
        
        self.assertRaises(TypeError, self.adapter.setSpeed, "10")
        self.assertRaises(TypeError, self.adapter.setSpeed, True)
        self.assertRaises(TypeError, self.adapter.setSpeed, False)
        self.assertRaises(TypeError, self.adapter.setSpeed, 0.8)
        self.assertRaises(IllegalArgumentError, self.adapter.setSpeed, None)
    