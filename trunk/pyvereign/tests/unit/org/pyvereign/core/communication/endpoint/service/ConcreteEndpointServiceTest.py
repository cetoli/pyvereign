from org.pyvereign.core.communication.endpoint.service.DefaultEndpointService import DefaultEndpointService
from org.pyvereign.core.communication.endpoint.service.ConcreteEndpointService import ConcreteEndpointService
from org.pyvereign.core.microkernel.Microkernel import Microkernel
from org.pyvereign.core.id.IDFactory import IDFactory
from org.pyvereign.util.Constants import Constants
from org.pyvereign.core.microkernel.CoreServiceContext import CoreServiceContext
from org.pyvereign.core.communication.endpoint.listener.EndpointListener import EndpointListener
from org.pyvereign.core.exception.EndpointServiceError import EndpointServiceError
from org.pyvereign.core.communication.endpoint.protocol.EndpointProtocol import EndpointProtocol
from org.pyvereign.core.communication.endpoint.protocol.MessageSender import MessageSender
import unittest

class ConcreteEndpointServiceTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(ConcreteEndpointService(DefaultEndpointService()))
        service = ConcreteEndpointService(DefaultEndpointService())
        self.assertEquals(DefaultEndpointService.NON_INITIALIZED, service.getStatus())
        
    def test_initialize_service(self):
        service = ConcreteEndpointService(DefaultEndpointService())
        self.assertEquals(DefaultEndpointService.NON_INITIALIZED, service.getStatus())
        kernel = Microkernel()
        kernel.initialize()
        
        self.assertTrue(kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION)))
        communication = kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION))
        
        service.initialize(communication, IDFactory().createCoreServiceID(communication, Constants.ENDPOINT_SERVICE), CoreServiceContext(service))
        
        self.assertEquals(DefaultEndpointService.INITIALIZED, service.getStatus())
    
    def test_start_service(self):
        service = ConcreteEndpointService(DefaultEndpointService())
        self.assertEquals(DefaultEndpointService.NON_INITIALIZED, service.getStatus())
        kernel = Microkernel()
        self.assertEquals(Microkernel.NON_INITIALIZED, kernel.getStatus())
        kernel.initialize()
        self.assertEquals(Microkernel.INITIALIZED, kernel.getStatus())
        self.assertTrue(kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION)))
        communication = kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION))
        
        service.initialize(communication, IDFactory().createCoreServiceID(communication, Constants.ENDPOINT_SERVICE), CoreServiceContext(service))
        self.assertEquals(DefaultEndpointService.INITIALIZED, service.getStatus())
        service.start([])
        self.assertEquals(DefaultEndpointService.STARTED, service.getStatus())
        
    def test_stop_service(self):
        service = ConcreteEndpointService(DefaultEndpointService())
        self.assertEquals(DefaultEndpointService.NON_INITIALIZED, service.getStatus())
        kernel = Microkernel()
        kernel.initialize()
        
        self.assertTrue(kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION)))
        communication = kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION))
        
        service.initialize(communication, IDFactory().createCoreServiceID(communication, Constants.ENDPOINT_SERVICE), CoreServiceContext(service))
        self.assertEquals(DefaultEndpointService.INITIALIZED, service.getStatus())
        service.start([])
        self.assertEquals(DefaultEndpointService.STARTED, service.getStatus())
        service.stop()
        self.assertEquals(DefaultEndpointService.STOPED, service.getStatus())
        
    def test_add_endpoint_listener(self):
        service = ConcreteEndpointService(DefaultEndpointService())
        self.assertEquals(DefaultEndpointService.NON_INITIALIZED, service.getStatus())
        kernel = Microkernel()
        self.assertEquals(Microkernel.NON_INITIALIZED, kernel.getStatus())
        kernel.initialize()
        self.assertTrue(kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION)))
        communication = kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION))
        service.initialize(communication, IDFactory().createCoreServiceID(communication, Constants.ENDPOINT_SERVICE), CoreServiceContext(service))
        self.assertEquals(DefaultEndpointService.INITIALIZED, service.getStatus())
        
        listener = EndpointListenerForTest()

        self.assertEquals(listener, service.addEndpointListener("TCP://127.0.0.1:5050", listener))
        self.assertTrue(service.hasEndpointListener("TCP://127.0.0.1:5050"))
        self.assertEquals(listener, service.getEndpointListener("TCP://127.0.0.1:5050"))
    
    def test_try_add_endpoint_listener_with_none_uri(self):
        self.assertRaises(TypeError, ConcreteEndpointService(DefaultEndpointService()).addEndpointListener, None, EndpointListenerForTest())
        
    def test_try_add_endpoint_listener_with_none_listener(self):
        self.assertRaises(TypeError, ConcreteEndpointService(DefaultEndpointService()).addEndpointListener, "TCP://127.0.0.1:5050", None)
        
    def test_try_add_endpoint_listener_with_invalid_type_uri(self):
        self.assertRaises(TypeError, ConcreteEndpointService(DefaultEndpointService()).addEndpointListener, 123, EndpointListenerForTest())
    
    def test_try_add_endpoint_listener_with_invalid_type_listener(self):
        self.assertRaises(TypeError, ConcreteEndpointService(DefaultEndpointService()).addEndpointListener, "TCP://127.0.0.1:5050", "listener")
        
    def test_remove_endpoint_listener(self):
        service = ConcreteEndpointService(DefaultEndpointService())
        self.assertEquals(DefaultEndpointService.NON_INITIALIZED, service.getStatus())
        kernel = Microkernel()
        self.assertEquals(Microkernel.NON_INITIALIZED, kernel.getStatus())
        kernel.initialize()
        self.assertTrue(kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION)))
        communication = kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION))
        service.initialize(communication, IDFactory().createCoreServiceID(communication, Constants.ENDPOINT_SERVICE), CoreServiceContext(service))
        self.assertEquals(DefaultEndpointService.INITIALIZED, service.getStatus())
        
        listener = EndpointListenerForTest()
        
        self.assertEquals(listener, service.addEndpointListener("TCP://127.0.0.1:5050", listener))
        self.assertTrue(service.hasEndpointListener("TCP://127.0.0.1:5050"))
        self.assertEquals(listener, service.getEndpointListener("TCP://127.0.0.1:5050"))
        
        self.assertEquals(listener, service.removeEndpointListener("TCP://127.0.0.1:5050"))
        self.assertFalse(service.hasEndpointListener("TCP://127.0.0.1:5050"))
    
    def test_try_remove_endpoint_listener_with_none_uri(self):
        self.assertRaises(TypeError, ConcreteEndpointService(DefaultEndpointService()).removeEndpointListener, 1233)
        
    def test_try_remove_endpoint_listener_with_invalid_type_for_uri(self):
        self.assertRaises(TypeError, ConcreteEndpointService(DefaultEndpointService()).removeEndpointListener, None) 
    
    def test_get_message_sender_tcp_ip_port(self):
        service = ConcreteEndpointService(DefaultEndpointService())
        self.assertEquals(DefaultEndpointService.NON_INITIALIZED, service.getStatus())
        kernel = Microkernel()
        self.assertEquals(Microkernel.NON_INITIALIZED, kernel.getStatus())
        kernel.initialize()
        self.assertTrue(kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION)))
        communication = kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION))
        service.initialize(communication, IDFactory().createCoreServiceID(communication, Constants.ENDPOINT_SERVICE), CoreServiceContext(service))
        self.assertEquals(DefaultEndpointService.INITIALIZED, service.getStatus())
        
        self.assertTrue(service.getMessageSender("TCP://127.0.0.0:5050"))
        self.assertTrue(isinstance(service.getMessageSender("TCP://127.0.0.0:5050"), MessageSender))
        sender = service.getMessageSender("TCP://127.0.0.0:5050")
        self.assertEquals("TCP://127.0.0.0:5050/", sender.getEndpointAddress().toURI())
    
    def test_get_message_sender_tcp_ip_port_service(self):
        service = ConcreteEndpointService(DefaultEndpointService())
        self.assertEquals(DefaultEndpointService.NON_INITIALIZED, service.getStatus())
        kernel = Microkernel()
        self.assertEquals(Microkernel.NON_INITIALIZED, kernel.getStatus())
        kernel.initialize()
        self.assertTrue(kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION)))
        communication = kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION))
        service.initialize(communication, IDFactory().createCoreServiceID(communication, Constants.ENDPOINT_SERVICE), CoreServiceContext(service))
        self.assertEquals(DefaultEndpointService.INITIALIZED, service.getStatus())
        
        self.assertTrue(service.getMessageSender("TCP://127.0.0.0:5050/service"))
        self.assertTrue(isinstance(service.getMessageSender("TCP://127.0.0.0:5050/service"), MessageSender))
        sender = service.getMessageSender("TCP://127.0.0.0:5050/service")
        self.assertEquals("TCP://127.0.0.0:5050/service", sender.getEndpointAddress().toURI())
        
    def test_get_message_sender_tcp_ip_port_service_action(self):
        service = ConcreteEndpointService(DefaultEndpointService())
        self.assertEquals(DefaultEndpointService.NON_INITIALIZED, service.getStatus())
        kernel = Microkernel()
        self.assertEquals(Microkernel.NON_INITIALIZED, kernel.getStatus())
        kernel.initialize()
        self.assertTrue(kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION)))
        communication = kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION))
        service.initialize(communication, IDFactory().createCoreServiceID(communication, Constants.ENDPOINT_SERVICE), CoreServiceContext(service))
        self.assertEquals(DefaultEndpointService.INITIALIZED, service.getStatus())
        
        self.assertTrue(service.getMessageSender("TCP://127.0.0.0:5050/service/action"))
        self.assertTrue(isinstance(service.getMessageSender("TCP://127.0.0.0:5050/service/action"), MessageSender))
        sender = service.getMessageSender("TCP://127.0.0.0:5050/service/action")
        self.assertEquals("TCP://127.0.0.0:5050/service/action", sender.getEndpointAddress().toURI())
    
    def test_get_message_sender_tcp_ip_port_service_action_parameter(self):
        service = ConcreteEndpointService(DefaultEndpointService())
        self.assertEquals(DefaultEndpointService.NON_INITIALIZED, service.getStatus())
        kernel = Microkernel()
        self.assertEquals(Microkernel.NON_INITIALIZED, kernel.getStatus())
        kernel.initialize()
        self.assertTrue(kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION)))
        communication = kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION))
        service.initialize(communication, IDFactory().createCoreServiceID(communication, Constants.ENDPOINT_SERVICE), CoreServiceContext(service))
        self.assertEquals(DefaultEndpointService.INITIALIZED, service.getStatus())
        
        self.assertTrue(service.getMessageSender("TCP://127.0.0.0:5050/service/action/parameter"))
        self.assertTrue(isinstance(service.getMessageSender("TCP://127.0.0.0:5050/service/action/parameter"), MessageSender))
        sender = service.getMessageSender("TCP://127.0.0.0:5050/service/action/parameter")
        self.assertEquals("TCP://127.0.0.0:5050/service/action/parameter", sender.getEndpointAddress().toURI())
    
    def test_get_message_sender_udp_ip_port(self):
        service = ConcreteEndpointService(DefaultEndpointService())
        self.assertEquals(DefaultEndpointService.NON_INITIALIZED, service.getStatus())
        kernel = Microkernel()
        self.assertEquals(Microkernel.NON_INITIALIZED, kernel.getStatus())
        kernel.initialize()
        self.assertTrue(kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION)))
        communication = kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION))
        service.initialize(communication, IDFactory().createCoreServiceID(communication, Constants.ENDPOINT_SERVICE), CoreServiceContext(service))
        self.assertEquals(DefaultEndpointService.INITIALIZED, service.getStatus())
        
        self.assertTrue(service.getMessageSender("UDP://127.0.0.0:5050"))
        self.assertTrue(isinstance(service.getMessageSender("UDP://127.0.0.0:5050"), MessageSender))
        sender = service.getMessageSender("UDP://127.0.0.0:5050")
        self.assertEquals("UDP://127.0.0.0:5050/", sender.getEndpointAddress().toURI())
    
    def test_get_message_sender_udp_ip_port_service(self):
        service = ConcreteEndpointService(DefaultEndpointService())
        self.assertEquals(DefaultEndpointService.NON_INITIALIZED, service.getStatus())
        kernel = Microkernel()
        self.assertEquals(Microkernel.NON_INITIALIZED, kernel.getStatus())
        kernel.initialize()
        self.assertTrue(kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION)))
        communication = kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION))
        service.initialize(communication, IDFactory().createCoreServiceID(communication, Constants.ENDPOINT_SERVICE), CoreServiceContext(service))
        self.assertEquals(DefaultEndpointService.INITIALIZED, service.getStatus())
        
        self.assertTrue(service.getMessageSender("UDP://127.0.0.0:5050/service"))
        self.assertTrue(isinstance(service.getMessageSender("UDP://127.0.0.0:5050/service"), MessageSender))
        sender = service.getMessageSender("UDP://127.0.0.0:5050/service")
        self.assertEquals("UDP://127.0.0.0:5050/service", sender.getEndpointAddress().toURI())
        
    def test_get_message_sender_udp_ip_port_service_action(self):
        service = ConcreteEndpointService(DefaultEndpointService())
        self.assertEquals(DefaultEndpointService.NON_INITIALIZED, service.getStatus())
        kernel = Microkernel()
        self.assertEquals(Microkernel.NON_INITIALIZED, kernel.getStatus())
        kernel.initialize()
        self.assertTrue(kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION)))
        communication = kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION))
        service.initialize(communication, IDFactory().createCoreServiceID(communication, Constants.ENDPOINT_SERVICE), CoreServiceContext(service))
        self.assertEquals(DefaultEndpointService.INITIALIZED, service.getStatus())
        
        self.assertTrue(service.getMessageSender("UDP://127.0.0.0:5050/service/action"))
        self.assertTrue(isinstance(service.getMessageSender("UDP://127.0.0.0:5050/service/action"), MessageSender))
        sender = service.getMessageSender("UDP://127.0.0.0:5050/service/action")
        self.assertEquals("UDP://127.0.0.0:5050/service/action", sender.getEndpointAddress().toURI())
    
    def test_get_message_sender_udp_ip_port_service_action_parameter(self):
        service = ConcreteEndpointService(DefaultEndpointService())
        self.assertEquals(DefaultEndpointService.NON_INITIALIZED, service.getStatus())
        kernel = Microkernel()
        self.assertEquals(Microkernel.NON_INITIALIZED, kernel.getStatus())
        kernel.initialize()
        self.assertTrue(kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION)))
        communication = kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION))
        service.initialize(communication, IDFactory().createCoreServiceID(communication, Constants.ENDPOINT_SERVICE), CoreServiceContext(service))
        self.assertEquals(DefaultEndpointService.INITIALIZED, service.getStatus())
        
        self.assertTrue(service.getMessageSender("UDP://127.0.0.0:5050/service/action/parameter"))
        self.assertTrue(isinstance(service.getMessageSender("UDP://127.0.0.0:5050/service/action/parameter"), MessageSender))
        sender = service.getMessageSender("UDP://127.0.0.0:5050/service/action/parameter")
        self.assertEquals("UDP://127.0.0.0:5050/service/action/parameter", sender.getEndpointAddress().toURI())
    
    def test_get_message_sender_udp_broadcast_port(self):
        service = ConcreteEndpointService(DefaultEndpointService())
        self.assertEquals(DefaultEndpointService.NON_INITIALIZED, service.getStatus())
        kernel = Microkernel()
        self.assertEquals(Microkernel.NON_INITIALIZED, kernel.getStatus())
        kernel.initialize()
        self.assertTrue(kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION)))
        communication = kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION))
        service.initialize(communication, IDFactory().createCoreServiceID(communication, Constants.ENDPOINT_SERVICE), CoreServiceContext(service))
        self.assertEquals(DefaultEndpointService.INITIALIZED, service.getStatus())
        
        self.assertTrue(service.getMessageSender("UDP://<broadcast>:5050"))
        self.assertTrue(isinstance(service.getMessageSender("UDP://<broadcast>:5050"), MessageSender))
    
    def test_get_message_sender_udp_broadcast_port_service(self):
        service = ConcreteEndpointService(DefaultEndpointService())
        self.assertEquals(DefaultEndpointService.NON_INITIALIZED, service.getStatus())
        kernel = Microkernel()
        self.assertEquals(Microkernel.NON_INITIALIZED, kernel.getStatus())
        kernel.initialize()
        self.assertTrue(kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION)))
        communication = kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION))
        service.initialize(communication, IDFactory().createCoreServiceID(communication, Constants.ENDPOINT_SERVICE), CoreServiceContext(service))
        self.assertEquals(DefaultEndpointService.INITIALIZED, service.getStatus())
        
        self.assertTrue(service.getMessageSender("UDP://<broadcast>:5050/service"))
        self.assertTrue(isinstance(service.getMessageSender("UDP://<broadcast>:5050/service"), MessageSender))
        
    def test_get_message_sender_udp_broadcast_port_service_action(self):
        service = ConcreteEndpointService(DefaultEndpointService())
        self.assertEquals(DefaultEndpointService.NON_INITIALIZED, service.getStatus())
        kernel = Microkernel()
        self.assertEquals(Microkernel.NON_INITIALIZED, kernel.getStatus())
        kernel.initialize()
        self.assertTrue(kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION)))
        communication = kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION))
        service.initialize(communication, IDFactory().createCoreServiceID(communication, Constants.ENDPOINT_SERVICE), CoreServiceContext(service))
        self.assertEquals(DefaultEndpointService.INITIALIZED, service.getStatus())
        
        self.assertTrue(service.getMessageSender("UDP://<broadcast>:5050/service/action"))
        self.assertTrue(isinstance(service.getMessageSender("UDP://<broadcast>:5050/service/action"), MessageSender))
    
    def test_get_message_sender_udp_broadcast_port_service_action_parameter(self):
        service = ConcreteEndpointService(DefaultEndpointService())
        self.assertEquals(DefaultEndpointService.NON_INITIALIZED, service.getStatus())
        kernel = Microkernel()
        self.assertEquals(Microkernel.NON_INITIALIZED, kernel.getStatus())
        kernel.initialize()
        self.assertTrue(kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION)))
        communication = kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION))
        service.initialize(communication, IDFactory().createCoreServiceID(communication, Constants.ENDPOINT_SERVICE), CoreServiceContext(service))
        self.assertEquals(DefaultEndpointService.INITIALIZED, service.getStatus())
        
        self.assertTrue(service.getMessageSender("UDP://<broadcast>:5050/service/action/parameter"))
        self.assertTrue(isinstance(service.getMessageSender("UDP://<broadcast>:5050/service/action/parameter"), MessageSender))
    
    def test_try_get_message_sender_with_none_uri(self):
        self.assertRaises(TypeError, ConcreteEndpointService(DefaultEndpointService()).getMessageSender, None)
    
    def test_try_get_message_sender_with_invalid_type_in_uri(self):
        self.assertRaises(TypeError, ConcreteEndpointService(DefaultEndpointService()).getMessageSender, 123)
    
    def test_get_endpoint_protocol_tcp(self):
        service = ConcreteEndpointService(DefaultEndpointService())
        self.assertEquals(DefaultEndpointService.NON_INITIALIZED, service.getStatus())
        kernel = Microkernel()
        self.assertEquals(Microkernel.NON_INITIALIZED, kernel.getStatus())
        kernel.initialize()
        self.assertTrue(kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION)))
        communication = kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION))
        service.initialize(communication, IDFactory().createCoreServiceID(communication, Constants.ENDPOINT_SERVICE), CoreServiceContext(service))
        self.assertEquals(DefaultEndpointService.INITIALIZED, service.getStatus())
        
        self.assertTrue(service.getEndpointProtocolByName("TCP"))
        self.assertTrue(isinstance(service.getEndpointProtocolByName("TCP"), EndpointProtocol))
        self.assertEquals("TCP", service.getEndpointProtocolByName("TCP").getName())
        
    def test_get_endpoint_protocol_UDP(self):
        service = ConcreteEndpointService(DefaultEndpointService())
        self.assertEquals(DefaultEndpointService.NON_INITIALIZED, service.getStatus())
        kernel = Microkernel()
        self.assertEquals(Microkernel.NON_INITIALIZED, kernel.getStatus())
        kernel.initialize()
        self.assertTrue(kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION)))
        communication = kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION))
        service.initialize(communication, IDFactory().createCoreServiceID(communication, Constants.ENDPOINT_SERVICE), CoreServiceContext(service))
        self.assertEquals(DefaultEndpointService.INITIALIZED, service.getStatus())
        
        self.assertTrue(service.getEndpointProtocolByName("UDP"))
        self.assertTrue(isinstance(service.getEndpointProtocolByName("UDP"), EndpointProtocol))
        self.assertEquals("UDP", service.getEndpointProtocolByName("UDP").getName())
        
    def test_try_get_endpoint_protocol_with_none_name(self):
        self.assertRaises(TypeError, ConcreteEndpointService(DefaultEndpointService()).getEndpointProtocolByName, None)
    
    def test_try_get_endpoint_protocol_with_invalid_type_in_name(self):
        self.assertRaises(TypeError, ConcreteEndpointService(DefaultEndpointService()).getEndpointProtocolByName, 123)
    
    def test_try_get_endpoint_protocol_with_non_existent_name(self):
        self.assertRaises(EndpointServiceError, ConcreteEndpointService(DefaultEndpointService()).getEndpointProtocolByName, "FTP")
    
    def test_get_endpoint_protocols(self):
        service = ConcreteEndpointService(DefaultEndpointService())
        self.assertEquals(DefaultEndpointService.NON_INITIALIZED, service.getStatus())
        kernel = Microkernel()
        self.assertEquals(Microkernel.NON_INITIALIZED, kernel.getStatus())
        kernel.initialize()
        self.assertTrue(kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION)))
        communication = kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION))
        service.initialize(communication, IDFactory().createCoreServiceID(communication, Constants.ENDPOINT_SERVICE), CoreServiceContext(service))
        self.assertEquals(DefaultEndpointService.INITIALIZED, service.getStatus())
        
        self.assertTrue(len(service.getEndpointProtocols()) > 0)
        
        
class EndpointListenerForTest(EndpointListener):
    
    def __init__(self):
        self._e = 1