from atlas.api.env.service.NetworkControllerService import NetworkControllerService
import unittest

class NetworkControllerServiceTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, NetworkControllerService)