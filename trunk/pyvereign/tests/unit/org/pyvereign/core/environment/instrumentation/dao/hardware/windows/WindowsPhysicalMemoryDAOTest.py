from org.pyvereign.core.environment.instrumentation.dao.hardware.windows.WindowsPhysicalMemoryDAO import WindowsPhysicalMemoryDAO
import unittest

class WindowsPhysicalMemoryDAOTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(WindowsPhysicalMemoryDAO())
        
    def test_retrieve_phisical_memories(self):
        memories = WindowsPhysicalMemoryDAO().retrievePhysicalMemories()
        self.assertTrue(memories)
        
        for physicalMemory in memories:
            self.assertTrue(physicalMemory.getCapacity())
            self.assertTrue(physicalMemory.getDataWidth())
            self.assertTrue(physicalMemory.getDescription())
            self.assertTrue(physicalMemory.getDeviceLocator())
            self.assertTrue(physicalMemory.getHardwareId())
            self.assertTrue(physicalMemory.getLogicalName())
            self.assertTrue(physicalMemory.getProduct())
            self.assertTrue(physicalMemory.getSerial())
            self.assertTrue(physicalMemory.getSpeed())
            self.assertTrue(physicalMemory.getVendor())