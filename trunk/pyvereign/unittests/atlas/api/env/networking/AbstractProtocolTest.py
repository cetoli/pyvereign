from atlas.api.env.networking.AbstractProtocol import AbstractProtocol
import unittest

class AbstractProtocolTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, AbstractProtocol)