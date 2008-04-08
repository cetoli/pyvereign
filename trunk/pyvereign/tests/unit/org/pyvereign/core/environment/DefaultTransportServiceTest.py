from org.pyvereign.core.environment.DefaultTransportService import DefaultTransportService
from org.pyvereign.core.environment.transport.listener.TransportListener import TransportListener
from org.pyvereign.core.environment.Environment import Environment
from org.pyvereign.core.id.IDFactory import IDFactory
from org.pyvereign.core.environment.transport.address.IPv4Address import IPv4Address
from org.pyvereign.core.context.Context import Context
from org.pyvereign.core.environment.DefaultInstrumentationService import DefaultInstrumentationService
from org.pyvereign.core.environment.transport.address.BroadcastIPv4Address import BroadcastIPv4Address
from org.pyvereign.core.exception.TransportError import TransportError
import unittest

class DefaultTransportServiceTest(unittest.TestCase):
    
    def setUp(self):
        self.service = DefaultTransportService()
        self.environment = environment = Environment()
        
        inst = DefaultInstrumentationService()
        instID = IDFactory().createCoreServiceID(environment, inst.getName())
        
        environment.addModule(instID, inst)
        self.service.initialize(environment, IDFactory().createCoreServiceID(environment, self.service.getName()), DefaultTransportServiceTest.ContextForTest())
    
    def test_send_stream_by_using_datagram_forwarder_in_unicast_mode(self):
        self.assertEquals("a", self.service.sendStream("UDP", IPv4Address("127.0.0.1", 5050), "a"))
    
    def test_send_stream_by_using_datagram_forwarder_in_broadcast_mode(self):
        self.assertEquals("b", self.service.sendStream("UDP", BroadcastIPv4Address(5050), "b", True))
        
    def test_try_send_by_using_tuple_with_ipaddress_port(self):
        self.assertRaises(TypeError, self.service.sendStream, "UDP", ("127.0.0.1", 5050), "test_try_send_by_using_tuple_with_ipaddress_port")
    
    def test_try_send_stream_with_incorrect_ip_address(self):
        self.assertRaises(TransportError, self.service.sendStream, "UDP", IPv4Address("127.0.0", 5050), "test transport service broadcast")
    
    def test_try_send_none_stream(self):
        self.assertRaises(RuntimeError, self.service.sendStream, "UDP", IPv4Address("127.0.0.1", 5050), None)
    
    def test_try_send_non_string_stream(self):
        self.assertRaises(TypeError, self.service.sendStream, "UDP", IPv4Address("127.0.0.1", 5050), 1111)
    
    def test_try_send_stream_over_UDP_protocol_with_invalid_time_out(self):
        self.assertRaises(TransportError, self.service.sendStream, "UDP", IPv4Address("127.0.0.1", 5050), "test", False, -1)
    
    def test_send_stream_by_using_stream_forwarder(self):
        self.assertEquals("c", self.service.sendStream("TCP", IPv4Address("127.0.0.1", 5050), "c"))
    
    def test_try_broadcasting_stream_with_stream_forwarder(self):
        self.assertRaises(TransportError, self.service.sendStream, "TCP", BroadcastIPv4Address(5050), "test transport service", True)
    
    def test_send_stream_with_broadcasting_parameter_configured_with_true_value(self):
        self.assertRaises(TransportError, self.service.sendStream, "TCP", IPv4Address("127.0.0.1", 5050), "test transport service", True)
    
    def test_send_stream_by_using_stream_forwarder_with_timeout(self):
        self.assertEquals("d", self.service.sendStream("TCP", IPv4Address("127.0.0.1", 5050), "d", False, 1))
    
    def test_try_send_stream_over_TCP_protocol_with_invalid_time_out(self):
        self.assertRaises(TransportError, self.service.sendStream, "TCP", IPv4Address("127.0.0.1", 5050), "test", False, -1)
    
    def test_try_send_stream_over_TCP_protocol_with_timeout(self):
        self.assertRaises(TransportError, self.service.sendStream, "TCP", IPv4Address("192.168.1.10", 5050), "test", False, 1)
    
    
    def test_get_number_of_transport_listeners(self):
        self.assertEquals(0, self.service.getNumberOfTransportListeners())
        listener = DefaultTransportServiceTest.TransportListenerForTest()
        self.assertEquals(listener, self.service.addTransportListener("TCP", "TCP://127.0.0.1:5050", listener))
        self.assertEquals(1, self.service.getNumberOfTransportListeners())
        self.assertEquals(listener, self.service.addTransportListener("UDP", "UDP://127.0.0.1:5050", listener))
        self.assertEquals(2, self.service.getNumberOfTransportListeners())
        self.assertEquals(listener, self.service.removeTransportListener("TCP", "TCP://127.0.0.1:5050"))
        self.assertEquals(1, self.service.getNumberOfTransportListeners())
        self.assertEquals(listener, self.service.removeTransportListener("UDP", "UDP://127.0.0.1:5050"))
        self.assertEquals(0, self.service.getNumberOfTransportListeners())

    def test_try_add_transport_listener_with_none_protocol(self):
        self.assertRaises(RuntimeError, DefaultTransportService().addTransportListener, None, "TCP://127.0.0.1:5050", DefaultTransportServiceTest.TransportListenerForTest())
    
    def test_try_add_transport_listener_with_none_uri(self):
        self.assertRaises(RuntimeError, DefaultTransportService().addTransportListener, "TCP", None, DefaultTransportServiceTest.TransportListenerForTest())
        
    def test_try_add_transport_listener_with_none_listener(self):
        self.assertRaises(RuntimeError, DefaultTransportService().addTransportListener, "TCP", "TCP://127.0.0.1:5050", None)
        
    def test_try_add_transport_listener_with_invalid_protocol_name(self):
        self.assertRaises(TypeError, DefaultTransportService().addTransportListener, 123, "TCP://127.0.0.1:5050", DefaultTransportServiceTest.TransportListenerForTest())
        
    def test_try_add_transport_listener_with_invalid_uri(self):
        self.assertRaises(TypeError, DefaultTransportService().addTransportListener, "TCP", 127.0, DefaultTransportServiceTest.TransportListenerForTest())
        
    def test_try_add_transport_listener_with_invalid_listener(self):
        self.assertRaises(TypeError, DefaultTransportService().addTransportListener, "TCP", "TCP://127.0.0.1:5050", "listener")
    
    def test_try_get_transport_listener_with_none_protocol_name(self):
        self.assertRaises(RuntimeError, DefaultTransportService().getTransportListener, None, "TCP://127.0.0.1:5050")
        
    def test_try_get_transport_listener_with_none_uri(self):
        self.assertRaises(RuntimeError, DefaultTransportService().getTransportListener, "TCP", None)
        
    def test_try_remove_transport_listener_with_none_protocol_name(self):
        self.assertRaises(RuntimeError, DefaultTransportService().getTransportListener, None, "TCP://127.0.0.1:5050")
        
    def test_try_remove_transport_listener_with_none_uri(self):
        self.assertRaises(RuntimeError, DefaultTransportService().getTransportListener, "TCP", None)
        
    def test_try_get_transport_listener_with_invalid_protocol_name(self):
        self.assertRaises(TypeError, DefaultTransportService().getTransportListener, 123, "TCP://127.0.0.1:5050")
    
    def test_try_get_transport_listener_with_invalid_uri(self):
        self.assertRaises(TypeError, DefaultTransportService().getTransportListener, "TCP", 123)
        
    def test_try_remove_transport_listener_with_invalid_protocol_name(self):
        self.assertRaises(TypeError, DefaultTransportService().removeTransportListener, 123, "TCP://127.0.0.1:5050")
    
    def test_try_remove_transport_listener_with_invalid_uri(self):
        self.assertRaises(TypeError, DefaultTransportService().removeTransportListener, "TCP", 123)
        
        
    class TransportListenerForTest(TransportListener):
        
        def __init__(self):
            self._stream = ""
        
        def processStream(self, stream):
            self._stream = stream
    
    class ContextForTest(Context):
        
        def __init__(self):
            return