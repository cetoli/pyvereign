from atlas.api.env.AbstractEnvironmentDataSource import AbstractEnvironmentDataSource
import unittest

class AbstractEnvironmentDataSourceTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, AbstractEnvironmentDataSource)