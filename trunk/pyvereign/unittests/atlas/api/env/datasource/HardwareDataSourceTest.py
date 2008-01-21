from atlas.api.env.datasource.HardwareDataSource import HardwareDataSource
import unittest

class HardwareDataSourceTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, HardwareDataSource)