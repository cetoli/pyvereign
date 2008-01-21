from atlas.api.env.service.DefaultNetworkControllerService import DefaultNetworkControllerService
from atlas.api.env.datasource.impl.windows.WindowsNetworkControllerDataSource import WindowsNetworkControllerDataSource
import unittest

class DefaultNetworkControllerServiceTest(unittest.TestCase):
    
    def test_create_service(self):
        self.assertTrue(DefaultNetworkControllerService())
        
    def test_retrieve_network_controllers(self):
        service = DefaultNetworkControllerService()
        dataSource = WindowsNetworkControllerDataSource()
        
        service.initialize()
        self.assertEquals(dataSource, service.setDataSource(dataSource))
        service.start()
        self.assertTrue(service.getNetworkControllers())
        self.assertEquals(2, len(service.getNetworkControllers()))