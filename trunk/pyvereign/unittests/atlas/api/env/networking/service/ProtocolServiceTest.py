from atlas.api.env.networking.service.ProtocolService import ProtocolService
import unittest

class ProtocolServiceTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, ProtocolService)