from atlas.api.env.hardware.service.AbstractHardwareService import AbstractHardwareService
import unittest

class AbstractHardwareServiceTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, AbstractHardwareService)