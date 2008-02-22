from atlas.api.env.transport.service.DefaultTransportService import DefaultTransportService
from atlas.api.env.transport.address.IPv4Address import IPv4Address
from atlas.api.env.transport.address.BroadcastIPv4Address import BroadcastIPv4Address
from atlas.api.exception.TransportError import TransportError
from atlas.api.env.Environment import Environment
import time
import unittest

environment = Environment()
environment.initialize()
environment.start()

service = DefaultTransportService()
service.initialize(environment)
service.start()

class DefaultTransportServiceTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(DefaultTransportService())
    
    def test_send_stream_by_using_datagram_forwarder_in_unicast_mode(self):
        self.assertEquals("a", service.sendStream("UDP", IPv4Address("127.0.0.1", 5050), "a"))
    
    def test_send_stream_by_using_datagram_forwarder_in_broadcast_mode(self):
        self.assertEquals("b", service.sendStream("UDP", BroadcastIPv4Address(5050), "b", True))
        
    def test_try_send_by_using_tuple_with_ipaddress_port(self):
        self.assertRaises(TypeError, service.sendStream, "UDP", ("127.0.0.1", 5050), "test_try_send_by_using_tuple_with_ipaddress_port")
    
    def test_try_send_stream_with_incorrect_ip_address(self):
        self.assertRaises(TransportError, service.sendStream, "UDP", IPv4Address("127.0.0", 5050), "test transport service broadcast")
    
    def test_try_send_none_stream(self):
        self.assertRaises(RuntimeError, service.sendStream, "UDP", IPv4Address("127.0.0.1", 5050), None)
    
    def test_try_send_non_string_stream(self):
        self.assertRaises(TypeError, service.sendStream, "UDP", IPv4Address("127.0.0.1", 5050), 1111)
    
    def test_try_send_stream_over_UDP_protocol_with_invalid_time_out(self):
        self.assertRaises(TransportError, service.sendStream, "UDP", IPv4Address("127.0.0.1", 5050), "test", False, -1)
    
    def test_send_stream_by_using_stream_forwarder(self):
        self.assertEquals("c", service.sendStream("TCP", IPv4Address("127.0.0.1", 5050), "c"))
    
    def test_try_broadcasting_stream_with_stream_forwarder(self):
        self.assertRaises(TransportError, service.sendStream, "TCP", BroadcastIPv4Address(5050), "test transport service", True)
    
    def test_send_stream_with_broadcasting_parameter_configured_with_true_value(self):
        self.assertRaises(TransportError, service.sendStream, "TCP", IPv4Address("127.0.0.1", 5050), "test transport service", True)
    
    def test_send_stream_by_using_stream_forwarder_with_timeout(self):
        self.assertEquals("d", service.sendStream("TCP", IPv4Address("127.0.0.1", 5050), "d", False, 1))
    
    def test_try_send_stream_over_TCP_protocol_with_invalid_time_out(self):
        self.assertRaises(TransportError, service.sendStream, "TCP", IPv4Address("127.0.0.1", 5050), "test", False, -1)
    
    def test_try_send_stream_over_TCP_protocol_with_timeout(self):
        self.assertRaises(TransportError, service.sendStream, "TCP", IPv4Address("192.168.1.10", 5050), "test", False, 1)
    
