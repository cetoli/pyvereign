from org.pyvereign.core.environment.instrumentation.dto.networking.NetworkProtocolImpl import NetworkProtocolImpl
import unittest

class NetworkProtocolImplTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(NetworkProtocolImpl({}))
        
        values = {"name": "TCP", "supportsBroadcasting": False,
                  "supportsMulticasting": False, "guaranteesDelivery": True
                 }
        
        protocol = NetworkProtocolImpl(values)
        self.assertEquals("TCP", protocol.getName())
        self.assertEquals(False, protocol.supportsMulticasting())
        self.assertEquals(False, protocol.supportsBroadcasting())
        self.assertEquals(True, protocol.guaranteesDelivery())
        
    def test_try_create_instance(self):
        self.assertRaises(RuntimeError, NetworkProtocolImpl, {"test": 123})
        