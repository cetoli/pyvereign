from atlas.api.env.transport.communicationapi.AbstractInetAddress import AbstractInetAddress
import unittest

class AbstractInetAddressTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, AbstractInetAddress)