from atlas.api.env.networking.datasource.impl.WindowsProtocolDataSource import WindowsProtocolDataSource
import unittest

class WindowsProtocolDataSourceTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(WindowsProtocolDataSource())
    
    def test_retrieve_protocols(self):
        datasource = WindowsProtocolDataSource()
        protocols = datasource.retrieveProtocols()
        self.assertTrue(protocols)
        self.assertTrue(len(protocols) > 0)
        
        self.assertEquals("TCP", protocols[0].getName())
        self.assertEquals("UDP", protocols[1].getName())