from atlas.api.env.hardware.datasource.impl.windows.WindowsNetworkControllerDataSource import WindowsNetworkControllerDataSource
import unittest

class WindowsNetworkControllerDataSourceTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(WindowsNetworkControllerDataSource())
        
    def test_retrieve_netwoork_controllers(self):
        ds = WindowsNetworkControllerDataSource()
        controllers = ds.retrieveNetworkControllers()
        self.assertEquals(2, len(controllers))