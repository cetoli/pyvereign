from atlas.api.env.datasource.AbstractHardwareDataSource import AbstractHardwareDataSource
import unittest

class AbstractHardwareDataSourceTest(unittest.TestCase):
    
    def test_try_create(self):
        self.assertRaises(NotImplementedError, AbstractHardwareDataSource)