from org.pyvereign.core.environment.dao.hardware.windows.WindowsHardwareDAOFactory import WindowsHardwareDAOFactory
from org.pyvereign.core.environment.dao.hardware.AbstractHardwareDAOFactory import AbstractHardwareDAOFactory
import unittest

class AbstractHardwareDAOFactoryTest(unittest.TestCase):
    
    def test_get_WindowsHardwareDAOFactory(self):
        self.assertEquals(WindowsHardwareDAOFactory, AbstractHardwareDAOFactory.getHardwareDAOFactory("nt").__class__)