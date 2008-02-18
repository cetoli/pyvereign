from atlas.api.com.endpoint.protocol.EndpointProtocol import EndpointProtocol
from atlas.api.env.networking.DefaultProtocol import DefaultProtocol
import unittest

class EndpointProtocolTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(EndpointProtocol(DefaultProtocol()))
        
    def test_try_create_instance_with_none_protocol(self):
        self.assertRaises(RuntimeError, EndpointProtocol, None)
        
    def test_try_create_instance_with_invalid_type_of_protocol(self):
        self.assertRaises(TypeError, EndpointProtocol, ("192.168.1.15", 5050))