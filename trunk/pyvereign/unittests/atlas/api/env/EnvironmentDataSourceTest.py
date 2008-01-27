from atlas.api.env.EnvironmentDataSource import EnvironmentDataSource
import unittest

class EnvironmentDataSourceTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, EnvironmentDataSource)