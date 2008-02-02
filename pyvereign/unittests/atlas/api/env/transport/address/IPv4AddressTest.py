from atlas.api.env.transport.address.IPv4Address import IPv4Address
import socket
import unittest

class IPv4AddressTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(IPv4Address("192.168.0.10", 5000))
    
    def test_values_of_instance(self):
        ip = IPv4Address("192.168.0.10", 5000)
        print ip.getFamily()
        self.assertEquals(socket.AF_INET, ip.getFamily())
        self.assertEquals("192.168.0.10", ip.getIPAddress())
        self.assertEquals(5000, ip.getPort())