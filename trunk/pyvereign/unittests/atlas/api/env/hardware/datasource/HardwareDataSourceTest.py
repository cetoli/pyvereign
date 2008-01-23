from atlas.api.env.hardware.datasource.HardwareDataSource import HardwareDataSource
import unittest

class HardwareDataSourceTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, HardwareDataSource)