from org.pyvereign.core.environment.instrumentation.dao.networking.windows.WindowsNetworkingElementDAOFactory import WindowsNetworkingElementDAOFactory
import unittest


class WindowsNetworkingElementDAOFactoryTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(WindowsNetworkingElementDAOFactory())