from org.pyvereign.core.environment.service.ConcreteTransportService import ConcreteTransportService
from org.pyvereign.core.environment.service.DefaultTransportService import DefaultTransportService
from org.pyvereign.core.environment.Environment import Environment
from org.pyvereign.core.id.IDFactory import IDFactory
from org.pyvereign.core.environment.service.DefaultNetworkingService import DefaultNetworkingService
from org.pyvereign.core.environment.transport.address.IPv4Address import IPv4Address
from org.pyvereign.core.environment.transport.address.BroadcastIPv4Address import BroadcastIPv4Address
from org.pyvereign.core.exception.TransportError import TransportError
from org.pyvereign.core.context.Context import Context
from org.pyvereign.core.environment.transport.listener.TransportListener import TransportListener
from org.pyvereign.core.microkernel.Microkernel import Microkernel
import unittest

class ConcreteTransportServiceTest(unittest.TestCase):
    
    def setUp(self):
        Microkernel().initialize()
        
        default = DefaultTransportService()
        self.service = ConcreteTransportService(default)
        self.environment = Environment()
        self.id = IDFactory().createCoreServiceID(self.environment.getName(), self.service.getName())
        self.environment.addModule(self.id, self.service)
        
        self.netService = DefaultNetworkingService()
        self.idNetService = IDFactory().createCoreServiceID(self.environment.getName(), self.netService.getName())
        self.environment.addModule(self.idNetService, self.netService)
        
        self.netService.initialize(self.environment, self.idNetService, ContextForTest())
        self.service.initialize(self.environment, self.id, ContextForTest())
        
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
        listener = TransportListenerForTest()
        self.assertEquals(listener, self.service.addTransportListener("TCP", "TCP://127.0.0.1:5050", listener))
        self.assertEquals(1, self.service.getNumberOfTransportListeners())
        self.assertEquals(listener, self.service.addTransportListener("UDP", "UDP://127.0.0.1:5050", listener))
        self.assertEquals(2, self.service.getNumberOfTransportListeners())
        self.assertEquals(listener, self.service.removeTransportListener("TCP", "TCP://127.0.0.1:5050"))
        self.assertEquals(1, self.service.getNumberOfTransportListeners())
        self.assertEquals(listener, self.service.removeTransportListener("UDP", "UDP://127.0.0.1:5050"))
        self.assertEquals(0, self.service.getNumberOfTransportListeners())

    def test_start_and_stop_service(self):
        self.assertEquals(DefaultTransportService.INITIALIZED, self.service.getStatus())
        self.service.start([6000])
        self.assertEquals(DefaultTransportService.STARTED, self.service.getStatus())
        self.service.stop()
        self.assertEquals(DefaultTransportService.STOPED, self.service.getStatus())
        
    
        
class ContextForTest(Context):
    
    def __init__(self):
        return

class TransportListenerForTest(TransportListener):
        
        def __init__(self):
            self._stream = ""
        
        def processStream(self, stream):
            self._stream = stream        