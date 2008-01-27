from atlas.api.env.networking.datasource.AbstractProtocolDataSource import AbstractProtocolDataSource
import unittest

class AbstractProtocolDataSourceTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, AbstractProtocolDataSource)