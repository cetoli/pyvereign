from org.pyvereign.core.environment.dao.hardware.windows.WindowsHardwareDAOFactory import WindowsHardwareDAOFactory
from org.pyvereign.core.environment.dao.hardware.AbstractHardwareDAOFactory import AbstractHardwareDAOFactory
import unittest

class AbstractHardwareDAOFactoryTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, AbstractHardwareDAOFactory)
    
    def test_get_WindowsHardwareDAOFactory(self):
        self.assertEquals(WindowsHardwareDAOFactory, AbstractHardwareDAOFactory.getHardwareDAOFactory("nt").__class__)