from org.pyvereign.environment.instrumentation.dataaccess.windows.windows_network_adapter_dao import WindowsNetworkAdapterDAO
from org.pyvereign.base.interface import implements
from org.pyvereign.environment.instrumentation.dataaccess.inetwork_adapter_dao import INetworkAdapterDAO
import unittest

class WindowsNetworkAdapterDAOTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(WindowsNetworkAdapterDAO())
        self.assertTrue(implements(WindowsNetworkAdapterDAO(), INetworkAdapterDAO))
    
    def test_retrieve_network_adapters(self):
        dao = WindowsNetworkAdapterDAO()
        self.assertTrue(dao.retrieveNetworkAdapters())
        self.assertTrue(len(dao.retrieveNetworkAdapters())  > 0)
        
        netAdapters = dao.retrieveNetworkAdapters()
        
        for adapter in netAdapters:
            self.assertTrue(adapter.getDescription() <> None)
            self.assertTrue(adapter.getHardwareId() <> None)
            self.assertTrue(adapter.getLogicalName() <> None)
            self.assertTrue(adapter.getProduct() <> None)
            self.assertTrue(adapter.getSerial() <> None)
            self.assertTrue(adapter.getVendor() <> None)
            self.assertTrue(adapter.getIPAddress() <> None)
            self.assertTrue(adapter.getMACAddress() <> None)
            self.assertTrue(adapter.getSpeed() > 0)
