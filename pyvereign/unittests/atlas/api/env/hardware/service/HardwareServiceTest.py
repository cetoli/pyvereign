from atlas.api.env.hardware.service.HardwareService import HardwareService
import unittest

class HardwareServiceTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, HardwareService)
    