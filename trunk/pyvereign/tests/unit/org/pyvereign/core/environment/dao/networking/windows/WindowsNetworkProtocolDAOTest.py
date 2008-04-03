from org.pyvereign.core.environment.dao.networking.windows.WindowsNetworkProtocolDAO import WindowsNetworkProtocolDAO
import unittest

class WindowsNetworkDAOProtocolTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(WindowsNetworkProtocolDAO())
        
    def test_retrieve_protocols(self):
        dao = WindowsNetworkProtocolDAO()
        self.assertTrue(dao.retrieveNetworkProtocols())
        
        protocols = dao.retrieveNetworkProtocols()
        
        for protocol in protocols:
            self.assertTrue(protocol.getName())
            self.assertTrue(protocol.supportsBroadcasting() <> None)
            self.assertTrue(protocol.supportsMulticasting() <> None)
            self.assertTrue(protocol.guaranteesDelivery() <> None)