from atlas.api.com.endpoint.protocol.EndpointProtocol import EndpointProtocol
from atlas.api.env.networking.DefaultProtocol import DefaultProtocol
from atlas.api.com.endpoint.address.EndpointAddress import EndpointAddress
from atlas.api.com.endpoint.format.JSONMessageFormat import JSONMessageFormat
from atlas.api.com.endpoint.protocol.MessageSender import MessageSender
import unittest

class EndpointProtocolTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(EndpointProtocol(DefaultProtocol()))
        
    def test_try_create_instance_with_none_protocol(self):
        self.assertRaises(RuntimeError, EndpointProtocol, None)
        
    def test_try_create_instance_with_invalid_type_of_protocol(self):
        self.assertRaises(TypeError, EndpointProtocol, ("192.168.1.15", 5050))
        
    def test_create_message_sender(self):
        protocol = EndpointProtocol(DefaultProtocol())
        self.assertTrue(protocol.getMessageSender(EndpointAddress("TCP", "192.168.1.12", 5000), JSONMessageFormat()))
        self.assertEquals(MessageSender, protocol.getMessageSender(EndpointAddress("TCP", "192.168.1.12", 5000), JSONMessageFormat()).__class__)