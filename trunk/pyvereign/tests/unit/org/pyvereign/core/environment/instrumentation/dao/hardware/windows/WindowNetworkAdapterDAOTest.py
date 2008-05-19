from org.pyvereign.core.environment.instrumentation.dao.hardware.windows.WindowsNetworkAdapterDAO import WindowsNetwworkAdapterDAO
import unittest

class WindowsNetworkAdapterDAOTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(WindowsNetwworkAdapterDAO())
        
    def test_retrieve_network_adapter(self):
        dao = WindowsNetwworkAdapterDAO()
        adapters = dao.retrieveNetworkAdapters()
        self.assertTrue(adapters <> None)
        self.assertTrue(len(adapters) >= 1)
        
        for adapter in adapters:
            self.assertTrue(adapter.getDescription())
            self.assertTrue(adapter.getProduct())
            self.assertTrue(adapter.getHardwareId())
            self.assertTrue(adapter.getSerial())
            self.assertTrue(adapter.getVendor())
            self.assertTrue(adapter.getMACAddress())
            self.assertTrue(adapter.getIPAddress())
            self.assertTrue(adapter.getSpeed() <> None)
            self.assertTrue(adapter.getLogicalName())
        