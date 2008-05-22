from org.pyvereign.core.communication.endpoint.protocol.EndpointProtocolImpl import EndpointProtocolImpl
from org.pyvereign.core.environment.instrumentation.dto.networking.NetworkProtocolImpl import NetworkProtocolImpl
from org.pyvereign.core.communication.format.JSONFormat import JSONFormat
from org.pyvereign.core.microkernel.Microkernel import Microkernel
from org.pyvereign.core.communication.endpoint.address.EndpointAddress import EndpointAddress
import unittest

class EndpointProtocolImplTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(EndpointProtocolImpl(NetworkProtocolImpl({"name": "TCP"})))
        self.assertTrue(EndpointProtocolImpl(NetworkProtocolImpl({"name": "UDP"})))
        
    def test_try_create_instance_with_none_protocol(self):
        self.assertRaises(TypeError, EndpointProtocolImpl, None)
        
    def test_try_create_instance_with_invalid_type_protocol(self):
        self.assertRaises(TypeError, EndpointProtocolImpl, "TCP")
        
    def test_get_name(self):
        self.assertTrue(EndpointProtocolImpl(NetworkProtocolImpl({"name": "TCP"})))
        self.assertEquals("TCP", EndpointProtocolImpl(NetworkProtocolImpl({"name": "TCP"})).getName())
        
        self.assertTrue(EndpointProtocolImpl(NetworkProtocolImpl({"name": "UDP"})))
        self.assertEquals("UDP", EndpointProtocolImpl(NetworkProtocolImpl({"name": "UDP"})).getName())
    
    def test_get_message_sender(self):
        protocol = EndpointProtocolImpl(NetworkProtocolImpl({"name": "TCP"}))
        self.assertTrue(protocol.getMessageSender(EndpointAddress("TCP", "192.068.1.5", 5050), Microkernel()))
        protocol = EndpointProtocolImpl(NetworkProtocolImpl({"name": "UDP"}))
        self.assertTrue(protocol.getMessageSender(EndpointAddress("UDP", "192.068.1.5", 5050), Microkernel()))
    
    def test_try_get_message_sender_with_none_endpoint_address(self):
        protocol = EndpointProtocolImpl(NetworkProtocolImpl({"name": "TCP"}))
        self.assertRaises(TypeError, protocol.getMessageSender, None, Microkernel())
        protocol = EndpointProtocolImpl(NetworkProtocolImpl({"name": "UDP"}))
        self.assertRaises(TypeError, protocol.getMessageSender, None, Microkernel())
    
    def test_try_get_message_sender_with_none_kernel(self):
        protocol = EndpointProtocolImpl(NetworkProtocolImpl({"name": "TCP"}))
        self.assertRaises(TypeError, protocol.getMessageSender, EndpointAddress("TCP", "192.068.1.5", 5050), JSONFormat(), None)
        protocol = EndpointProtocolImpl(NetworkProtocolImpl({"name": "UDP"}))
        self.assertRaises(TypeError, protocol.getMessageSender, EndpointAddress("UDP", "192.068.1.5", 5050), JSONFormat(), None)
    
    def test_try_get_message_sender_with_invalid_endpoint_address(self):
        protocol = EndpointProtocolImpl(NetworkProtocolImpl({"name": "TCP"}))
        self.assertRaises(TypeError, protocol.getMessageSender, "192.168.1.3", JSONFormat(), Microkernel())
        protocol = EndpointProtocolImpl(NetworkProtocolImpl({"name": "UDP"}))
        self.assertRaises(TypeError, protocol.getMessageSender, "192.168.1.3", JSONFormat(), Microkernel())
    
    def test_try_get_message_sender_with_invalid_format(self):
        protocol = EndpointProtocolImpl(NetworkProtocolImpl({"name": "TCP"}))
        self.assertRaises(TypeError, protocol.getMessageSender, EndpointAddress("TCP", "192.068.1.5", 5050), "JSON", Microkernel())
        protocol = EndpointProtocolImpl(NetworkProtocolImpl({"name": "UDP"}))
        self.assertRaises(TypeError, protocol.getMessageSender, EndpointAddress("UDP", "192.068.1.5", 5050), "JSON", Microkernel())
    
    def test_try_get_message_sender_with_invalid_kernel(self):
        protocol = EndpointProtocolImpl(NetworkProtocolImpl({"name": "TCP"}))
        self.assertRaises(TypeError, protocol.getMessageSender, EndpointAddress("TCP", "192.068.1.5", 5050), JSONFormat(), "kernel")
        protocol = EndpointProtocolImpl(NetworkProtocolImpl({"name": "UDP"}))
        self.assertRaises(TypeError, protocol.getMessageSender, EndpointAddress("UDP", "192.068.1.5", 5050), JSONFormat(), "kernel")
    