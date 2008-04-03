from org.pyvereign.core.environment.transport.address.BindIPv4Address import BindIPv4Address
import socket
import unittest

class BindIPv4AddressTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(BindIPv4Address(5000))
        
    def test_values_of_instance(self):
        ip = BindIPv4Address(5000)
        self.assertEquals(socket.AF_INET, ip.getFamily())
        self.assertEquals("127.0.0.1", ip.getIPAddress())
        self.assertEquals(5000, ip.getPort())