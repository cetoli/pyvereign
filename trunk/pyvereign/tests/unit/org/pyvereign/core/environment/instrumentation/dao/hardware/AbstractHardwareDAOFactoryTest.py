from org.pyvereign.core.environment.instrumentation.dao.hardware.AbstractHardwareDAOFactory import AbstractHardwareDAOFactory
from org.pyvereign.core.environment.instrumentation.dao.hardware.windows.WindowsHardwareDAOFactory import WindowsHardwareDAOFactory
import unittest

class AbstractHardwareDAOFactoryTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, AbstractHardwareDAOFactory)
    
    def test_get_WindowsHardwareDAOFactory(self):
        self.assertEquals(WindowsHardwareDAOFactory, AbstractHardwareDAOFactory.getHardwareDAOFactory("nt").__class__)