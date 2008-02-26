from atlas.api.com.endpoint.service.DefaultEndpointService import DefaultEndpointService
from atlas.api.com.endpoint.listener.EndpointListener import EndpointListener
from atlas.api.microkernel.Microkernel import Microkernel
from atlas.api.com.Communication import Communication
from atlas.api.com.endpoint.message.EndpointMessage import EndpointMessage
from atlas.api.com.endpoint.address.EndpointAddress import EndpointAddress
from atlas.api.com.endpoint.protocol.MessageSender import MessageSender
from atlas.api.com.endpoint.format.JSONMessageFormat import JSONMessageFormat
from atlas.api.com.endpoint.protocol.EndpointProtocol import EndpointProtocol
import unittest

Microkernel().initialize()
Microkernel().start()

class DefaultEndpointServiceTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(DefaultEndpointService())
        
    def test_add_endpoint_listener_with_tcp(self):
        service = DefaultEndpointService()
        self.assertEquals(DefaultEndpointService.NON_INITIALIZED, service.getStatus())
        service.initialize(Communication())
        self.assertEquals(DefaultEndpointService.INITIALIZED, service.getStatus())
        listener = DefaultEndpointServiceTest.EndpointListenerForTest()
        self.assertEquals(listener, service.addEndpointListener("TCP://127.0.0.1:5050", listener))
        self.assertEquals(1, service.getNumberOfEndpointListeners())
        
    def test_remove_endpoint_listener_with_tcp(self):
        service = DefaultEndpointService()
        self.assertEquals(DefaultEndpointService.NON_INITIALIZED, service.getStatus())
        service.initialize(Communication())
        self.assertEquals(DefaultEndpointService.INITIALIZED, service.getStatus())
        listener = DefaultEndpointServiceTest.EndpointListenerForTest()
        self.assertEquals(listener, service.addEndpointListener("TCP://127.0.0.1:5050", listener))
        self.assertEquals(1, service.getNumberOfEndpointListeners())
        
        self.assertEquals(listener, service.removeEndpointListener("TCP://127.0.0.1:5050"))
        self.assertEquals(0, service.getNumberOfEndpointListeners())
        
    def test_add_endpoint_listener_with_udp(self):
        service = DefaultEndpointService()
        self.assertEquals(DefaultEndpointService.NON_INITIALIZED, service.getStatus())
        service.initialize(Communication())
        self.assertEquals(DefaultEndpointService.INITIALIZED, service.getStatus())
        listener = DefaultEndpointServiceTest.EndpointListenerForTest()
        self.assertEquals(listener, service.addEndpointListener("UDP://127.0.0.1:5050", listener))
        self.assertEquals(1, service.getNumberOfEndpointListeners())
        
    def test_remove_endpoint_listener_with_udp(self):
        service = DefaultEndpointService()
        self.assertEquals(DefaultEndpointService.NON_INITIALIZED, service.getStatus())
        service.initialize(Communication())
        self.assertEquals(DefaultEndpointService.INITIALIZED, service.getStatus())
        listener = DefaultEndpointServiceTest.EndpointListenerForTest()
        self.assertEquals(listener, service.addEndpointListener("UDP://127.0.0.1:5050", listener))
        self.assertEquals(1, service.getNumberOfEndpointListeners())
        
        self.assertEquals(listener, service.removeEndpointListener("UDP://127.0.0.1:5050"))
        self.assertEquals(0, service.getNumberOfEndpointListeners())
        
    def test_create_endpoint_message(self):
        service = DefaultEndpointService()
        self.assertTrue(service.createEndpointMessage("TCP://127.0.0.1:5050", "TCP://127.0.0.1:5050"))
        self.assertEquals(EndpointMessage, service.createEndpointMessage("TCP://127.0.0.1:5050", "TCP://127.0.0.1:5050").__class__)
        message = service.createEndpointMessage("TCP://192.068.1.25:5050", "TCP://192.168.1.4:5050")
        self.assertEquals("TCP://192.068.1.25:5050", message.getOrigin().toURI())
        self.assertEquals("TCP://192.168.1.4:5050", message.getDestination().toURI())
    
    def test_try_create_endpoint_message_with_none_origin(self):
        service = DefaultEndpointService()
        self.assertRaises(RuntimeError, service.createEndpointMessage, None, "TCP://127.0.0.1:5050")
        
    def test_try_create_endpoint_message_with_none_destination(self):
        service = DefaultEndpointService()
        self.assertRaises(RuntimeError, service.createEndpointMessage, "TCP://127.0.0.1:5050", None)
    
    def test_try_create_endpoint_message_with_invalid_type_for_origin(self):
        service = DefaultEndpointService()
        self.assertRaises(TypeError, service.createEndpointMessage, 123, "TCP://192.068.1.25:5050")
        
    def test_try_create_endpoint_message_with_invalid_type_for_destination(self):
        service = DefaultEndpointService()
        self.assertRaises(TypeError, service.createEndpointMessage, "TCP://192.068.1.25:5050", 123)
    
    def test_try_create_endpoint_address_with_tcp_ip_port(self):
        service = DefaultEndpointService()
        self.assertTrue(service.createEndpointAddress("TCP://192.068.1.25:5050"))
        self.assertEquals(EndpointAddress, service.createEndpointAddress("TCP://192.068.1.25:5050").__class__)
        self.assertEquals("TCP://192.068.1.25:5050", service.createEndpointAddress("TCP://192.068.1.25:5050").toURI())
     
    def test_try_create_endpoint_address_with_tcp_ip_port_service(self):
        service = DefaultEndpointService()
        self.assertTrue(service.createEndpointAddress("TCP://192.068.1.25:5050/service"))
        self.assertEquals(EndpointAddress, service.createEndpointAddress("TCP://192.068.1.25:5050/service").__class__)
        self.assertEquals("TCP://192.068.1.25:5050/service", service.createEndpointAddress("TCP://192.068.1.25:5050/service").toURI())
    
    def test_try_create_endpoint_address_with_tcp_ip_port_service_parameters(self):
        service = DefaultEndpointService()
        self.assertTrue(service.createEndpointAddress("TCP://192.068.1.25:5050/service/parameters"))
        self.assertEquals(EndpointAddress, service.createEndpointAddress("TCP://192.068.1.25:5050/service/parameters").__class__)
        self.assertEquals("TCP://192.068.1.25:5050/service/parameters", service.createEndpointAddress("TCP://192.068.1.25:5050/service/parameters").toURI())   
    
    def test_try_create_endpoint_address_with_udp_ip_port(self):
        service = DefaultEndpointService()
        self.assertTrue(service.createEndpointAddress("UDP://192.068.1.25:5050"))
        self.assertEquals(EndpointAddress, service.createEndpointAddress("UDP://192.068.1.25:5050").__class__)
        self.assertEquals("UDP://192.068.1.25:5050", service.createEndpointAddress("UDP://192.068.1.25:5050").toURI())
     
    def test_try_create_endpoint_address_with_udp_ip_port_service(self):
        service = DefaultEndpointService()
        self.assertTrue(service.createEndpointAddress("UDP://192.068.1.25:5050/service"))
        self.assertEquals(EndpointAddress, service.createEndpointAddress("UDP://192.068.1.25:5050/service").__class__)
        self.assertEquals("UDP://192.068.1.25:5050/service", service.createEndpointAddress("UDP://192.068.1.25:5050/service").toURI())
    
    def test_try_create_endpoint_address_with_udp_ip_port_service_parameters(self):
        service = DefaultEndpointService()
        self.assertTrue(service.createEndpointAddress("UDP://192.068.1.25:5050/service/parameters"))
        self.assertEquals(EndpointAddress, service.createEndpointAddress("UDP://192.068.1.25:5050/service/parameters").__class__)
        self.assertEquals("UDP://192.068.1.25:5050/service/parameters", service.createEndpointAddress("UDP://192.068.1.25:5050/service/parameters").toURI())
    
    def test_create_enpoint_address_with_none_uri(self):
        service = DefaultEndpointService()
        self.assertRaises(RuntimeError, service.createEndpointAddress, None)
        
    def test_create_enpoint_address_with_invalid_type_for_uri(self):
        service = DefaultEndpointService()
        self.assertRaises(RuntimeError, service.createEndpointAddress, None)
        
    def test_get_message_sender(self):
        address = EndpointAddress.toEndpointAddress("UDP://192.068.1.25:5050/service")
        service = DefaultEndpointService()
        service.initialize(Communication())
        self.assertTrue(service.getMessageSender(address, JSONMessageFormat()))
        self.assertEquals(MessageSender, service.getMessageSender(address, JSONMessageFormat()).__class__)
        
    def test_try_get_message_sender_with_none_endpoint_address(self):
        address = EndpointAddress.toEndpointAddress("UDP://192.068.1.25:5050/service")
        service = DefaultEndpointService()
        service.initialize(Communication())
        self.assertRaises(RuntimeError, service.getMessageSender, None, JSONMessageFormat())
    
    def test_try_get_message_sender_with_none_format(self):
        address = EndpointAddress.toEndpointAddress("UDP://192.068.1.25:5050/service")
        service = DefaultEndpointService()
        service.initialize(Communication())
        self.assertRaises(RuntimeError, service.getMessageSender, address, None)
        
    def test_try_get_message_with_an_invalid_type_for_address(self):
        service = DefaultEndpointService()
        service.initialize(Communication())
        self.assertRaises(TypeError, service.getMessageSender, "UDP://192.068.1.25:5050/service", JSONMessageFormat())
    
    def test_try_get_message_with_an_invalid_type_for_format(self):
        address = EndpointAddress.toEndpointAddress("UDP://192.068.1.25:5050/service")
        service = DefaultEndpointService()
        service.initialize(Communication())
        self.assertRaises(TypeError, service.getMessageSender, address, "json")
        
    def test_get_protocol_name_with_tcp(self):
        service = DefaultEndpointService()
        service.initialize(Communication())
        self.assertTrue(service.getProtocolByName("TCP"))
        self.assertEquals(EndpointProtocol, service.getProtocolByName("TCP").__class__)
    
    def test_get_protocol_name_with_udp(self):
        service = DefaultEndpointService()
        service.initialize(Communication())
        self.assertTrue(service.getProtocolByName("UDP"))
        self.assertEquals(EndpointProtocol, service.getProtocolByName("UDP").__class__)
        
    def test_try_get_protocol_with_none_protocol_name(self):
        service = DefaultEndpointService()
        self.assertRaises(RuntimeError, service.getProtocolByName, None)
    
    def test_try_get_protocol_with_invalid_type_for_protocol_name(self):
        service = DefaultEndpointService()
        self.assertRaises(TypeError, service.getProtocolByName, 123)
        
    def test_get_endpoint_protocols(self):
        service = DefaultEndpointService()
        service.initialize(Communication())
        self.assertTrue(service.getEndpointProtocols())
    
    class EndpointListenerForTest(EndpointListener):
        
        def __init__(self):
            self._message = None
            
        def processMessage(self, message):
            self._message = message