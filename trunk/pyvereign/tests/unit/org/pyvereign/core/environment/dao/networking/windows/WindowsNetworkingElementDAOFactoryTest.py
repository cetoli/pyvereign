import unittest

from org.pyvereign.core.environment.dao.networking.windows.WindowsNetworkingElementDAOFactory import WindowsNetworkingElementDAOFactory 

class WindowsNetworkingElementDAOFactoryTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(WindowsNetworkingElementDAOFactory())