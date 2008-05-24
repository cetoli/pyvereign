from org.pyvereign.core.environment.instrumentation.dao.system.windows.WindowsSystemElementDAOFactory import WindowsSystemElementDAOFactory
from org.pyvereign.core.environment.instrumentation.dao.system.windows.WindowsProcessDAO import WindowsProcessDAO
import unittest

class WindowsSystemElementDAOFactoryTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(WindowsSystemElementDAOFactory())
        
    def test_create_process_dao(self):
        self.assertEquals(WindowsProcessDAO, WindowsSystemElementDAOFactory().createProcessDAO().__class__)