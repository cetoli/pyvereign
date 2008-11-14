from org.pyvereign.environment.instrumentation.dataaccess.windows.windows_data_access_factory import WindowsDataAccessFactory
from org.pyvereign.environment.instrumentation.dataaccess.idata_access_factory import IDataAccessFactory
from org.pyvereign.base.interface import implements
from org.pyvereign.environment.instrumentation.dataaccess.ibattery_dao import IBatteryDAO
from org.pyvereign.environment.instrumentation.hardware.idisk_drive import IDiskDrive
from org.pyvereign.environment.instrumentation.dataaccess.idisk_drive_dao import IDiskDriveDAO
from org.pyvereign.environment.instrumentation.dataaccess.imachine_dao import IMachineDAO
from org.pyvereign.environment.instrumentation.dataaccess.inetwork_adapter_dao import INetworkAdapterDAO
from org.pyvereign.environment.instrumentation.dataaccess.iphysical_memory_dao import IPhysicalMemoryDAO
from org.pyvereign.environment.instrumentation.dataaccess.iprocessor_dao import IProcessorDAO
import unittest

class WindowsDataAccessFactoryTest(unittest.TestCase):
    
    def test_create_windows_data_access_factory(self):
        factory = WindowsDataAccessFactory()
        self.assertTrue(implements(factory, IDataAccessFactory))
        
    def test_create_windows_battery_dao(self):
        factory = WindowsDataAccessFactory()
        self.assertTrue(implements(factory.createBatteryDAO(), IBatteryDAO))
        
    def test_create_windows_disk_drive_dao(self):
        factory = WindowsDataAccessFactory()
        self.assertTrue(implements(factory.createDiskDriveDAO(), IDiskDriveDAO))
    
    def test_create_windows_machine_dao(self):
        factory = WindowsDataAccessFactory()
        self.assertTrue(implements(factory.createMachineDAO(), IMachineDAO))
        
    def test_create_windows_network_adapter_dao(self):
        factory = WindowsDataAccessFactory()
        self.assertTrue(implements(factory.createNetworkAdapterDAO(), INetworkAdapterDAO))
    
    def test_create_windows_physical_memory_dao(self):
        factory = WindowsDataAccessFactory()
        self.assertTrue(implements(factory.createPhysicalMemoryDAO(), IPhysicalMemoryDAO))
        
    def test_create_windows_processor_dao(self):
        factory = WindowsDataAccessFactory()
        self.assertTrue(implements(factory.createProcessorDAO(), IProcessorDAO))
        