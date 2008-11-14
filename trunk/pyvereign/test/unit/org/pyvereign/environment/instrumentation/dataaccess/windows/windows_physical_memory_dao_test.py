from org.pyvereign.environment.instrumentation.dataaccess.windows.windows_physical_memory_dao import WindowsPhysicalMemoryDAO
from org.pyvereign.base.interface import implements
from org.pyvereign.environment.instrumentation.dataaccess.iphysical_memory_dao import IPhysicalMemodryDAO
import unittest

class WindowsPhysicalMemoryDAOTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(WindowsPhysicalMemoryDAO())
        self.assertTrue(implements(WindowsPhysicalMemoryDAO(), IPhysicalMemodryDAO))
    
    def test_retrieve_physical_memories(self):
        dao = WindowsPhysicalMemoryDAO()
        self.assertTrue(dao.retrievePhysicalMemories())
        self.assertTrue(len(dao.retrievePhysicalMemories()) > 0)
        
        memories = dao.retrievePhysicalMemories()
        
        for memory in memories:
            self.assertTrue(memory.getDescription() <> None)
            self.assertTrue(memory.getHardwareId() <> None)
            self.assertTrue(memory.getLogicalName() <> None)
            self.assertTrue(memory.getProduct() <> None)
            self.assertTrue(memory.getSerial() <> None)
            self.assertTrue(memory.getVendor() <> None)
            self.assertTrue(memory.getCapacity() > 0)
    
    
            
        