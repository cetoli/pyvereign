from org.pyvereign.core.environment.dao.hardware.windows.WindowsPhysicalMemoryDAO import WindowsPhysicalMemoryDAO
import unittest

class WindowsPhysicalMemoryDAOTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(WindowsPhysicalMemoryDAO())
        
    def test_retrieve_phisical_memories(self):
        memories = WindowsPhysicalMemoryDAO().retrievePhysicalMemories()
        self.assertTrue(memories)