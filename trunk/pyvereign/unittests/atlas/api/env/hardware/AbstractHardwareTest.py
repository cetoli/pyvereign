from atlas.api.env.hardware.AbstractHardware import AbstractHardware
import unittest

class AbstractHardwareTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, AbstractHardware)