from atlas.api.env.networking.Protocol import Protocol
import unittest

class ProtocolTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, Protocol)