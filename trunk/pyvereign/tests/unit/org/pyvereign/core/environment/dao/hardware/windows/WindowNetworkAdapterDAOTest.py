from org.pyvereign.core.environment.dao.hardware.windows.WindowsNetworkAdapterDAO import WindowsNetwworkAdapterDAO
import unittest

class WindowsNetworkAdapterDAOTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(WindowsNetwworkAdapterDAO())
        
    def test_retrieve_network_adapter(self):
        dao = WindowsNetwworkAdapterDAO()
        adapters = dao.retrieveNetworkAdapters()
        self.assertTrue(adapters)
        self.assertTrue(len(adapters) >= 1)
        
        for adapter in adapters:
            self.assertTrue(adapter.getDescription())
            self.assertTrue(adapter.getProduct())
            self.assertTrue(adapter.getHardwareId())
            self.assertTrue(adapter.getSerial())
            self.assertTrue(adapter.getVendor())
            self.assertTrue(adapter.getMACAddress())
            print adapter.getIPAddress()
            self.assertTrue(adapter.getIPAddress())
            self.assertTrue(adapter.getSpeed())
            self.assertTrue(adapter.getLogicalName())
        