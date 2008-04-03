from org.pyvereign.core.environment.transport.address.BroadcastIPv4Address import BroadcastIPv4Address
import socket
import unittest

class BroadcastIPv4AddressTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(BroadcastIPv4Address(5000))
    
    def test_values_of_instance(self):
        ip = BroadcastIPv4Address(5000)
        self.assertEquals(socket.AF_INET, ip.getFamily())
        self.assertEquals("<broadcast>", ip.getIPAddress())
        self.assertEquals(5000, ip.getPort())