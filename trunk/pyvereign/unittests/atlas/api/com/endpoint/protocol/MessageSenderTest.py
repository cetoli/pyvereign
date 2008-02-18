from atlas.api.com.endpoint.protocol.MessageSender import MessageSender
from atlas.api.com.endpoint.address.EndpointAddress import EndpointAddress
from atlas.api.com.endpoint.format.JSONMessageFormat import JSONMessageFormat
from atlas.api.com.endpoint.message.EndpointMessage import EndpointMessage
import unittest

class MessageSenderTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(MessageSender(EndpointAddress("TCP", "192.168.1.2", 5050), JSONMessageFormat()))
        
    def test_try_create_instance_with_none_endpoint_address(self):
        self.assertRaises(RuntimeError, MessageSender, None, JSONMessageFormat())
    
    def test_try_create_instance_with_none_format(self):
        self.assertRaises(RuntimeError, MessageSender, EndpointAddress("TCP", "192.168.1.2", 5050), None)
    
    def test_try_create_instance_with_invalid_type_of_address(self):
        self.assertRaises(TypeError, MessageSender, ("TCP", "192.168.1.2", 5050), JSONMessageFormat())
        
    def test_try_create_instance_with_invalid_type_of_format(self):
        self.assertRaises(TypeError, MessageSender, EndpointAddress("TCP", "192.168.1.2", 5050), "format")
    
    def test_send_message_with_tcp(self):
        address = EndpointAddress("TCP", "127.0.0.1", 5050)
        format = JSONMessageFormat()
        sender = MessageSender(address, format)
        message = EndpointMessage(address, address)
        
        self.assertEquals(message, sender.sendMessage(message))
    
    def test_send_message_with_udp_unicast_mode(self):
        address = EndpointAddress("UDP", "127.0.0.1", 5050)
        format = JSONMessageFormat()
        sender = MessageSender(address, format)
        message = EndpointMessage(address, address)
        
        self.assertEquals(message, sender.sendMessage(message))
        
    def test_send_message_with_udp_broadcast_mode(self):
        address = EndpointAddress("UDP", "<broadcast>", 5050)
        format = JSONMessageFormat()
        sender = MessageSender(address, format)
        message = EndpointMessage(address, address)
        
        self.assertEquals(message, sender.sendMessage(message))
        
    