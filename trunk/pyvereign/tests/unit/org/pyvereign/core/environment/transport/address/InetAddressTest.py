from org.pyvereign.core.environment.transport.address.InetAddress import InetAddress
import unittest

class InetAddressTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, InetAddress)