from atlas.api.env.hardware.HardwareFactory import HardwareFactory
import unittest

class HardwareFactoryTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(HardwareFactory())
        self.assertEquals(HardwareFactory(), HardwareFactory())
        