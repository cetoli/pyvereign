from atlas.api.env.hardware.service.DefaultNetworkControllerService import DefaultNetworkControllerService
from atlas.api.env.hardware.datasource.impl.windows.WindowsNetworkControllerDataSource import WindowsNetworkControllerDataSource
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
        controllers = service.getNetworkControllers()
        self.assertTrue(len(controllers) > 0)
        
    def test_get_network_controller(self):
        service = DefaultNetworkControllerService()
        dataSource = WindowsNetworkControllerDataSource()
        
        service.initialize()
        self.assertEquals(dataSource, service.setDataSource(dataSource))
        service.start()
        controllers = service.getNetworkControllers()
        
        ctrls = [x for x in controllers]
        self.assertTrue(len(ctrls) > 0)
        
        controller = ctrls[0]
        
        self.assertEquals(controller, service.getNetworkController(controller.getMACAddress()))
        
    def test_get_ipaddresses(self):
        service = DefaultNetworkControllerService()
        dataSource = WindowsNetworkControllerDataSource()
        
        service.initialize()
        self.assertEquals(dataSource, service.setDataSource(dataSource))
        service.start()
        controllers = service.getNetworkControllers()
        
        self.assertTrue(len(service.getIPAddresses()) > 0)
    
    def test_get_macaddresses(self):
        service = DefaultNetworkControllerService()
        dataSource = WindowsNetworkControllerDataSource()
        
        service.initialize()
        self.assertEquals(dataSource, service.setDataSource(dataSource))
        service.start()
        controllers = service.getNetworkControllers()
        
        self.assertTrue(len(service.getMACAddresses()) > 0)
        