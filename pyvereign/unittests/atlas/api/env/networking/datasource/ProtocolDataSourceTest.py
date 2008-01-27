from atlas.api.env.networking.datasource.ProtocolDataSource import ProtocolDataSource
import unittest

class ProtocolDataSourceTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, ProtocolDataSource)