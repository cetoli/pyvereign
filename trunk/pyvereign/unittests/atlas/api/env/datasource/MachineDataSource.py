from atlas.api.env.datasource.MachineDataSource import MachineDataSource
import unittest

class MachineDataSourceTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, MachineDataSource)