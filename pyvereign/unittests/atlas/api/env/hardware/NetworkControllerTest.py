from atlas.api.env.hardware.NetworkController import NetworkController
import unittest

class NetworkControllerTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, NetworkController)