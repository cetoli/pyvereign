from atlas.api.env.service.AbstractNetworkControllerService import AbstractNetworkControllerService
import unittest

class AbstractNetworkControllerServiceTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, AbstractNetworkControllerService)