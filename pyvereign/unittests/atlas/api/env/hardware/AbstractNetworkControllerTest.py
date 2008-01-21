from atlas.api.env.hardware.AbstractNetworkController import AbstractNetworkController
import unittest

class AbstractNetworkControllerTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, AbstractNetworkController)