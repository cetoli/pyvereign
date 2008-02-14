from atlas.api.env.hardware.service.DefaultMachineService import DefaultMachineService
from atlas.api.env.hardware.datasource.impl.windows.WindowsMachineDataSource import WindowsMachineDataSource
from atlas.api.env.Environment import Environment
import unittest

class DefaultMachineServiceTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(DefaultMachineService())
    
    def test_default_machine_service_with_windows_machine_data_source(self):
        service = DefaultMachineService()
        datasource = WindowsMachineDataSource()
        
        service.initialize(Environment())
        self.assertEquals(datasource, service.setDataSource(datasource))
        service.start()
        
        self.assertTrue(service.getDescription())
        self.assertTrue(service.getDomain())
        self.assertTrue(service.getLogicalName())
        self.assertTrue(service.getNumberOfProcessors())
        self.assertTrue(service.getProduct())
        self.assertTrue(service.getVendor())
        self.assertTrue(service.getTotalPhysicalMemory())
        self.assertTrue(service.getSerial())
        self.assertTrue(service)