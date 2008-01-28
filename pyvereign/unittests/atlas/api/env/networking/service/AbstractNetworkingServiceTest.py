from atlas.api.env.networking.service.AbstractNetworkingService import AbstractNetworkingService
import unittest

class AbstractNetworkingServiceTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, AbstractNetworkingService)