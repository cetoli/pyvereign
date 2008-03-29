from org.pyvereign.core.environment.dao.hardware.windows.WindowsHardwareDAOFactory import WindowsHardwareDAOFactory
from org.pyvereign.core.environment.dao.hardware.windows.WindowsDiskDriveDAO import WindowsDiskDriveDAO
from org.pyvereign.core.environment.dao.hardware.windows.WindowsMachineDAO import WindowsMachineDAO
from org.pyvereign.core.environment.dao.hardware.windows.WindowsPhysicalMemoryDAO import WindowsPhysicalMemoryDAO
from org.pyvereign.core.environment.dao.hardware.windows.WindowsProcessorDAO import WindowsProcessorDAO
import unittest

class WindowsHardwareDAOFactoryTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(WindowsHardwareDAOFactory())
        
    def test_createDiskDriveDAO(self):
        self.assertEquals(WindowsDiskDriveDAO, WindowsHardwareDAOFactory().createDiskDriveDAO().__class__)
    
    def test_createMachineDAO(self):
        self.assertEquals(WindowsMachineDAO, WindowsHardwareDAOFactory().createMachineDAO().__class__)
    
    def test_createPhysicalMemoryDAO(self):
        self.assertEquals(WindowsPhysicalMemoryDAO, WindowsHardwareDAOFactory().createPhysicalMemoryDAO().__class__)
    
    def test_createProcessorDAO(self):
        self.assertEquals(WindowsProcessorDAO, WindowsHardwareDAOFactory().createProcessorDAO().__class__)
    