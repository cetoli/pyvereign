from atlas.api.env.networking.service.AbstractProtocolService import AbstractProtocolService
import unittest

class AbstractProtocolServiceTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, AbstractProtocolService)