from atlas.api.env.datasource.AbstractMachineDataSource import AbstractMachineDataSource
import unittest

class AbstractMachineDataSourceTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, AbstractMachineDataSource)