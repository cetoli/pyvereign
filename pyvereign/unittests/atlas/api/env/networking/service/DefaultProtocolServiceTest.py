from atlas.api.env.networking.service.DefaultProtocolService import DefaultProtocolService
from atlas.api.env.networking.datasource.impl.windows.WindowsProtocolDataSource import WindowsProtocolDataSource
from atlas.api.env.Environment import Environment
import unittest

class DefaultProtocolServiceTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(DefaultProtocolService())
        
    def test_get_protocols(self):
        service = DefaultProtocolService()
        datasource = WindowsProtocolDataSource()
        self.assertEquals(datasource, service.setDataSource(datasource))
        service.initialize(Environment())
        
        service.start()
        protocols = service.getProtocols()
        self.assertTrue(len(protocols) > 0)
    
    def test_get_TCP_protocol(self):
        service = DefaultProtocolService()
        datasource = WindowsProtocolDataSource()
        self.assertEquals(datasource, service.setDataSource(datasource))
        service.initialize(Environment())
        
        service.start()
        
        self.assertTrue(service.getProtocol("TCP"))
        
        protocol = service.getProtocol("TCP")
        self.assertEquals("TCP", protocol.getName())
        self.assertFalse(protocol.supportsBroadcasting())
        
    def test_get_UDP_protocol(self):
        service = DefaultProtocolService()
        datasource = WindowsProtocolDataSource()
        self.assertEquals(datasource, service.setDataSource(datasource))
        service.initialize(Environment())
        service.start()
        
        self.assertTrue(service.getProtocol("UDP"))
        
        protocol = service.getProtocol("UDP")
        self.assertEquals("UDP", protocol.getName())
        self.assertTrue(protocol.supportsBroadcasting())