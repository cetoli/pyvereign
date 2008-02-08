from atlas.api.env.transport.forwarder.StreamForwarder import StreamForwarder
from atlas.api.env.transport.address.IPv4Address import IPv4Address
from atlas.api.env.networking.DefaultProtocol import DefaultProtocol
from atlas.api.env.transport.address.BindIPv4Address import BindIPv4Address
from atlas.api.env.transport.address.BroadcastIPv4Address import BroadcastIPv4Address
from atlas.api.exception.TransportError import TransportError
import unittest

class StreamForwarderTest(unittest.TestCase):
    
    def test_create_instance_ipv4_address(self):
        self.assertTrue(StreamForwarder(IPv4Address('192.168.1.2', 5050), DefaultProtocol()))
        
    def test_create_instance_bind_ipv4_address(self):
        self.assertTrue(StreamForwarder(BindIPv4Address(5050), DefaultProtocol()))
    
    def test_create_instance_broadcast_ipv4_address(self):
        self.assertRaises(TransportError, StreamForwarder, BroadcastIPv4Address(5050), DefaultProtocol())
    
    def test_create_instance_with_tuple(self):
        self.assertRaises(TypeError, StreamForwarder, ("192.168.1.2", 5050), DefaultProtocol())
    
    def test_try_create_instance_by_using_a_string_as_protocol(self):
        self.assertRaises(TypeError, StreamForwarder, IPv4Address("192.168.1.10", 5050), "TCP")
    
    def test_open_forwarder(self):
        forwarder = StreamForwarder(IPv4Address('192.168.1.2', 5050), DefaultProtocol())
        self.assertTrue(forwarder.getInetAddress())
        self.assertTrue(forwarder.getProtocol())
        self.assertTrue(forwarder.open())
        self.assertTrue(forwarder.close())
    
    def test_support_broadcasting_true(self):
        forwarder = StreamForwarder(IPv4Address('192.168.1.2', 5050), DefaultProtocol())
        self.assertRaises(TransportError, forwarder.supportBroadcasting, True)
        self.assertFalse(forwarder.isSupportingBroadcasting())
    
    def test_support_broadcasting_false(self):
        forwarder = StreamForwarder(IPv4Address('192.168.1.2', 5050), DefaultProtocol())
        self.assertRaises(TransportError, forwarder.supportBroadcasting, False)
        self.assertFalse(forwarder.isSupportingBroadcasting())
    
    def test_try_support_broadcasting_with_non_boolean_value(self):
        forwarder = StreamForwarder(IPv4Address("192.168.1.2", 5050), DefaultProtocol())
        self.assertTrue(forwarder.open())
        self.assertRaises(TransportError, forwarder.supportBroadcasting, "True")
        self.assertFalse(forwarder.isSupportingBroadcasting())
        self.assertTrue(forwarder.close())
        
    def test_try_support_broadcasting_with_none_value(self):
        forwarder = StreamForwarder(IPv4Address("192.168.1.2", 5050), DefaultProtocol())
        self.assertTrue(forwarder.open())
        self.assertRaises(TransportError, forwarder.supportBroadcasting, None)
        self.assertFalse(forwarder.isSupportingBroadcasting())
        self.assertTrue(forwarder.close())
    
    def test_send_stream_using_ipv4_address(self):
        forwarder = StreamForwarder(IPv4Address("192.168.1.2", 5050), DefaultProtocol())
        self.assertTrue(forwarder.open())
        self.assertTrue("test send stream", forwarder.send("test send stream"))
        self.assertTrue(forwarder.close())
        
    def test_send_stream_using_bind_ipv4_address(self):
        forwarder = StreamForwarder(BindIPv4Address(5050), DefaultProtocol())
        self.assertTrue(forwarder.open())
        self.assertTrue("test send stream with bind address", forwarder.send("test send stream with bind address"))
        self.assertTrue(forwarder.close())
    
    def test_try_sent_stream_to_inactive_address(self):
        forwarder = StreamForwarder(IPv4Address("192.168.1.10", 5050), DefaultProtocol())
        try:
            try:
                self.assertTrue(forwarder.open())
                self.assertRaises(TransportError, forwarder.send, "test forwarder")
            except:
                raise
        finally:
            self.assertTrue(forwarder.close())
        
    def test_try_send_stream_with_incorrect_ip_address(self):
        forwarder = StreamForwarder(IPv4Address("192.168.1", 5050), DefaultProtocol())
        try:
            try:
                self.assertTrue(forwarder.open())
                self.assertRaises(TransportError, forwarder.send, "test forwarder")
            except:
                raise
        finally:
            self.assertTrue(forwarder.close())
            
    def test_try_send_stream_with_non_opened_forwarder(self):
        forwarder = StreamForwarder(IPv4Address("192.168.1.2", 5050), DefaultProtocol())
        self.assertRaises(TransportError, forwarder.send, "test")
    
    def test_try_send_none_stream(self):
        forwarder = StreamForwarder(IPv4Address("192.168.1.2", 5050), DefaultProtocol())
        try:
            try:
                self.assertTrue(forwarder.open())
                self.assertRaises(RuntimeError, forwarder.send, None)
            except:
                raise
        finally:
            self.assertTrue(forwarder.close()) 
    
    def test_try_send_non_string_stream(self):
        forwarder = StreamForwarder(IPv4Address("192.168.1.2", 5050), DefaultProtocol())
        try:
            try:
                self.assertTrue(forwarder.open())
                self.assertRaises(TypeError, forwarder.send, 1111)
            except:
                raise
        finally:
            self.assertTrue(forwarder.close()) 
        
    def test_set_get_timeout(self):
        forwarder = StreamForwarder(IPv4Address("192.168.1.2", 5050), DefaultProtocol())
        self.assertTrue(forwarder.open())
        self.assertEquals(3, forwarder.setTimeout(3))
        self.assertTrue(forwarder.close())
    
    def test_try_set_get_timeout_with_non_opened_forwarder(self):
        forwarder = StreamForwarder(IPv4Address("192.168.1.2", 5050), DefaultProtocol())
        self.assertRaises(TransportError, forwarder.setTimeout, 3)
        self.assertRaises(TransportError, forwarder.getTimeout)
        
    def test_send_stream_with_configured_timeout(self):
        forwarder = StreamForwarder(IPv4Address("192.168.1.2", 5050), DefaultProtocol())
        self.assertTrue(forwarder.open())
        self.assertEquals(1, forwarder.setTimeout(1))
        self.assertEquals("timeout test", forwarder.send("timeout test"))
        self.assertTrue(forwarder.close())
        
    def test_try_send_stream_with_configured_timeout(self):
        forwarder = StreamForwarder(IPv4Address("192.168.1.10", 5050), DefaultProtocol())
        self.assertTrue(forwarder.open())
        self.assertEquals(1, forwarder.setTimeout(1))
        self.assertRaises(TransportError, forwarder.send, "timeout test")
        self.assertTrue(forwarder.close())
        
    def test_try_set_none_timeout_(self):
        forwarder = StreamForwarder(IPv4Address("192.168.1.2", 5050), DefaultProtocol())
        self.assertTrue(forwarder.open())
        self.assertRaises(RuntimeError, forwarder.setTimeout, None)
        self.assertTrue(forwarder.close())
    
    def test_try_set_string_timeout_(self):
        forwarder = StreamForwarder(IPv4Address("192.168.1.2", 5050), DefaultProtocol())
        self.assertTrue(forwarder.open())
        self.assertRaises(TypeError, forwarder.setTimeout, "1")
        self.assertTrue(forwarder.close())
        
    def test_try_set_invalid_timeout_with_zero_value(self):
        forwarder = StreamForwarder(IPv4Address("192.168.1.2", 5050), DefaultProtocol())
        self.assertTrue(forwarder.open())
        self.assertRaises(RuntimeError, forwarder.setTimeout, 0)
        self.assertTrue(forwarder.close())
        
    def test_try_set_invalid_timeout_with_negative_value(self):
        forwarder = StreamForwarder(IPv4Address("192.168.1.2", 5050), DefaultProtocol())
        self.assertTrue(forwarder.open())
        self.assertRaises(RuntimeError, forwarder.setTimeout, -1)
        self.assertTrue(forwarder.close())