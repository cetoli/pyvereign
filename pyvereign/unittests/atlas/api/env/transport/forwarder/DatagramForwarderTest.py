from atlas.api.env.transport.forwarder.DatagramForwarder import DatagramForwarder
from atlas.api.env.transport.address.IPv4Address import IPv4Address
from atlas.api.env.transport.address.BroadcastIPv4Address import BroadcastIPv4Address
from atlas.api.env.transport.address.BindIPv4Address import BindIPv4Address
from atlas.api.exception.TransportError import TransportError
from atlas.api.env.networking.DefaultProtocol import DefaultProtocol
import unittest

class DatagramForwarderTest(unittest.TestCase):
    
    def test_create_instance_with_ip_v4_address(self):
        self.assertTrue(DatagramForwarder(IPv4Address("192.168.1.10", 5050), DefaultProtocol()))
    
    def test_create_instance_with_broadcast_ip_v4_address(self):
        self.assertTrue(DatagramForwarder(BroadcastIPv4Address(5050), DefaultProtocol()))
        
    def test_create_instance_with_bind_v4_address(self):
        self.assertTrue(DatagramForwarder(BindIPv4Address(5050), DefaultProtocol()))
        
    def test_try_create_instance_with_tuple(self):
        self.assertRaises(TypeError, DatagramForwarder, ("192.168.1.10", 5050), DefaultProtocol())
        
    def test_try_create_instance_by_using_a_string_as_protocol(self):
        self.assertRaises(TypeError, DatagramForwarder, IPv4Address("192.168.1.10", 5050), "UDP")
        
    def test_open_forwarder(self):
        forwarder = DatagramForwarder(IPv4Address("192.168.1.2", 5050), DefaultProtocol())
        
        self.assertTrue(forwarder.getInetAddress())
        self.assertTrue(forwarder.open())
        self.assertTrue(forwarder.close())
    
    def test_support_broadcasting_true(self):
        forwarder = DatagramForwarder(IPv4Address("192.168.1.2", 5050), DefaultProtocol())
        self.assertTrue(forwarder.open())
        self.assertTrue(forwarder.supportBroadcasting(True))
        self.assertTrue(forwarder.isSupportingBroadcasting())
        self.assertTrue(forwarder.close())
    
    def test_support_broadcasting_false(self):
        forwarder = DatagramForwarder(IPv4Address("192.168.1.2", 5050), DefaultProtocol())
        self.assertTrue(forwarder.open())
        self.assertFalse(forwarder.supportBroadcasting(False))
        self.assertFalse(forwarder.isSupportingBroadcasting())
        self.assertTrue(forwarder.close())
    
    def test_try_support_broadcasting_with_non_boolean_value(self):
        forwarder = DatagramForwarder(IPv4Address("192.168.1.2", 5050), DefaultProtocol())
        self.assertTrue(forwarder.open())
        self.assertRaises(TypeError, forwarder.supportBroadcasting, "True")
        self.assertTrue(forwarder.close())
        
    def test_try_support_broadcasting_with_none_value(self):
        forwarder = DatagramForwarder(IPv4Address("192.168.1.2", 5050), DefaultProtocol())
        self.assertTrue(forwarder.open())
        self.assertRaises(RuntimeError, forwarder.supportBroadcasting, None)
        self.assertTrue(forwarder.close())
        
    def test_try_support_broadcasting_with_non_opened_forwarder(self):
        forwarder = DatagramForwarder(IPv4Address("192.168.1.2", 5050), DefaultProtocol())
        self.assertRaises(TransportError, forwarder.supportBroadcasting, True)
        
    def test_send_stream_by_using_unicast_mode(self):
        forwarder = DatagramForwarder(BindIPv4Address(5050), DefaultProtocol())
        try:
            try:
                self.assertTrue(forwarder.open())
                self.assertEquals("test forwarder", forwarder.send("test forwarder"))
            except:
                raise
        finally:
            self.assertTrue(forwarder.close())
            
    def test_try_send_stream_with_incorrect_ip_address(self):
        forwarder = DatagramForwarder(IPv4Address("192.168.1", 5050), DefaultProtocol())
        try:
            try:
                self.assertTrue(forwarder.open())
                self.assertRaises(TransportError, forwarder.send, "test forwarder")
            except:
                raise
        finally:
            self.assertTrue(forwarder.close())
            
    def test_try_send_stream_by_using_broadcasting_mode(self):
        forwarder = DatagramForwarder(BroadcastIPv4Address(5050), DefaultProtocol())
        try:
            try:
                self.assertTrue(forwarder.open())
                self.assertTrue(forwarder.supportBroadcasting(True))
                self.assertTrue(forwarder.isSupportingBroadcasting())
                self.assertEquals("test_try_send_stream_by_using_broadcasting_mode", forwarder.send("test_try_send_stream_by_using_broadcasting_mode"))
            except:
                raise
        finally:
            self.assertTrue(forwarder.close())
    
    def test_try_send_none_stream(self):
        forwarder = DatagramForwarder(BroadcastIPv4Address(5050), DefaultProtocol())
        try:
            try:
                self.assertTrue(forwarder.open())
                self.assertRaises(RuntimeError, forwarder.send, None)
            except:
                raise
        finally:
            self.assertTrue(forwarder.close()) 
    
    def test_try_send_non_string_stream(self):
        forwarder = DatagramForwarder(BroadcastIPv4Address(5050), DefaultProtocol())
        try:
            try:
                self.assertTrue(forwarder.open())
                self.assertRaises(TypeError, forwarder.send, 1111)
            except:
                raise
        finally:
            self.assertTrue(forwarder.close()) 
    
    def test_try_send_stream_with_non_opened_forwarder(self):
        forwarder = DatagramForwarder(IPv4Address("192.168.1", 5050), DefaultProtocol())
        self.assertRaises(TransportError, forwarder.send, "test forwarder")
    
    def test_send_stream_with_configured_timeout(self):
        forwarder = DatagramForwarder(IPv4Address("192.168.1.2", 5050), DefaultProtocol())
        self.assertTrue(forwarder.open())
        self.assertEquals(1, forwarder.setTimeout(1))
        self.assertEquals("timeout test", forwarder.send("timeout test"))
        self.assertTrue(forwarder.close())
    
    def test_try_send_stream_with_configured_timeout(self):
        forwarder = DatagramForwarder(IPv4Address("192.168.1.10", 5050), DefaultProtocol())
        self.assertTrue(forwarder.open())
        self.assertEquals(1, forwarder.setTimeout(1))
        self.assertEquals("timeout test", forwarder.send("timeout test"))
        self.assertTrue(forwarder.close())
        
    def test_try_set_none_timeout_(self):
        forwarder = DatagramForwarder(IPv4Address("192.168.1.2", 5050), DefaultProtocol())
        self.assertTrue(forwarder.open())
        self.assertRaises(RuntimeError, forwarder.setTimeout, None)
        self.assertTrue(forwarder.close())
    
    def test_try_set_string_timeout_(self):
        forwarder = DatagramForwarder(IPv4Address("192.168.1.2", 5050), DefaultProtocol())
        self.assertTrue(forwarder.open())
        self.assertRaises(TypeError, forwarder.setTimeout, "1")
        self.assertTrue(forwarder.close())
        
    def test_try_set_invalid_timeout_with_zero_value(self):
        forwarder = DatagramForwarder(IPv4Address("192.168.1.2", 5050), DefaultProtocol())
        self.assertTrue(forwarder.open())
        self.assertRaises(RuntimeError, forwarder.setTimeout, 0)
        self.assertTrue(forwarder.close())
        
    def test_try_set_invalid_timeout_with_negative_value(self):
        forwarder = DatagramForwarder(IPv4Address("192.168.1.2", 5050), DefaultProtocol())
        self.assertTrue(forwarder.open())
        self.assertRaises(RuntimeError, forwarder.setTimeout, -1)
        self.assertTrue(forwarder.close())
    
    
    
    