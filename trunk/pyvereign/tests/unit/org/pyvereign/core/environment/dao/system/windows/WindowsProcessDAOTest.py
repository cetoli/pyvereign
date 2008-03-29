from org.pyvereign.core.environment.dao.system.windows.WindowsProcessDAO import WindowsProcessDAO
import unittest

class WindowsProcessDAOTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(WindowsProcessDAO())
    
    def test_retrieve_processes(self):
        dao = WindowsProcessDAO()
        self.assertTrue(dao.retrieveProcesses())
        self.assertTrue(len(dao.retrieveProcesses()) >= 1)
        