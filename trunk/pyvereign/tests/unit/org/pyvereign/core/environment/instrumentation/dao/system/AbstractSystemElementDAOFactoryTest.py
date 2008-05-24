from org.pyvereign.core.environment.instrumentation.dao.system.AbstractSystemElementDAOFactory import AbstractSystemElementDAOFactory
from org.pyvereign.core.environment.instrumentation.dao.system.windows.WindowsSystemElementDAOFactory import WindowsSystemElementDAOFactory
import unittest

class AbstractSystemElementDAOFactoryTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, AbstractSystemElementDAOFactory)
        
    def test_get_system_element_dao_factory(self):
        self.assertEquals(WindowsSystemElementDAOFactory, AbstractSystemElementDAOFactory.getSystemElementDAOFactory("nt").__class__)