from atlas.api.env.hardware.Hardware import Hardware

import unittest

class HardwareTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, Hardware)