from atlas.api.env.transport.service.DefaultTransportService import DefaultTransportService
from atlas.api.env.transport.address.IPv4Address import IPv4Address
from atlas.api.env.transport.address.BroadcastIPv4Address import BroadcastIPv4Address
from atlas.api.exception.TransportError import TransportError
import unittest

class DefaultTransportServiceTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(DefaultTransportService())
    
    def test_send_stream_by_using_datagram_forwarder_in_unicast_mode(self):
        service = DefaultTransportService()
        self.assertEquals("test transport service", service.sendStream("UDP", IPv4Address("127.0.0.1", 5050), "test transport service"))
    
    def test_send_stream_by_using_datagram_forwarder_in_broadcast_mode(self):
        service = DefaultTransportService()
        self.assertEquals("test transport service broadcast", service.sendStream("UDP", BroadcastIPv4Address(5050), "test transport service broadcast", True))
        
    def test_try_send_by_using_tuple_with_ipaddress_port(self):
        service = DefaultTransportService()
        self.assertRaises(TypeError, service.sendStream, "UDP", ("127.0.0.1", 5050), "test_try_send_by_using_tuple_with_ipaddress_port")
    
    def test_try_send_stream_with_incorrect_ip_address(self):
        service = DefaultTransportService()
        self.assertRaises(TransportError, service.sendStream, "UDP", IPv4Address("127.0.0", 5050), "test transport service broadcast")
    
    def test_try_send_none_stream(self):
        service = DefaultTransportService()
        self.assertRaises(RuntimeError, service.sendStream, "UDP", IPv4Address("127.0.0.1", 5050), None)
    
    def test_try_send_non_string_stream(self):
        service = DefaultTransportService()
        self.assertRaises(TypeError, service.sendStream, "UDP", IPv4Address("127.0.0.1", 5050), 1111)
    
    def test_try_send_stream_over_UDP_protocol_with_invalid_time_out(self):
        service = DefaultTransportService()
        self.assertRaises(TransportError, service.sendStream, "UDP", IPv4Address("127.0.0.1", 5050), "test", False, -1)
    
    def test_send_stream_by_using_stream_forwarder(self):
        service = DefaultTransportService()
        self.assertEquals("test transport service", service.sendStream("TCP", IPv4Address("127.0.0.1", 5050), "test transport service"))
    
    def test_try_broadcasting_stream_with_stream_forwarder(self):
        service = DefaultTransportService()
        self.assertRaises(TransportError, service.sendStream, "TCP", BroadcastIPv4Address(5050), "test transport service", True)
    
    def test_send_stream_with_broadcasting_parameter_configured_with_true_value(self):
        service = DefaultTransportService()
        self.assertRaises(TransportError, service.sendStream, "TCP", IPv4Address("127.0.0.1", 5050), "test transport service", True)
    
    def test_send_stream_by_using_stream_forwarder_with_timeout(self):
        service = DefaultTransportService()
        self.assertEquals("test transport service timeout", service.sendStream("TCP", IPv4Address("127.0.0.1", 5050), "test transport service timeout", False, 1))
    
    def test_try_send_stream_over_TCP_protocol_with_invalid_time_out(self):
        service = DefaultTransportService()
        self.assertRaises(TransportError, service.sendStream, "TCP", IPv4Address("127.0.0.1", 5050), "test", False, -1)
    
    def test_try_send_stream_over_TCP_protocol_with_timeout(self):
        service = DefaultTransportService()
        self.assertRaises(TransportError, service.sendStream, "TCP", IPv4Address("192.168.1.10", 5050), "test", False, 1)