from atlas.api.com.endpoint.protocol.MessageReceiver import MessageReceiver
from atlas.api.com.endpoint.address.EndpointAddress import EndpointAddress
from atlas.api.com.endpoint.format.JSONMessageFormat import JSONMessageFormat
from atlas.api.com.endpoint.service.DefaultEndpointService import DefaultEndpointService
from atlas.api.com.endpoint.listener.EndpointListener import EndpointListener
from atlas.api.com.Communication import Communication
from atlas.api.microkernel.Microkernel import Microkernel
import json
import unittest

Microkernel().initialize()
Microkernel().start()

class MessageReceiverTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(MessageReceiver(EndpointAddress("TCP", "192.168.1.2", 5050), JSONMessageFormat(), DefaultEndpointService()))
        
    def test_try_create_instance_with_none_endpoint_address(self):
        self.assertRaises(RuntimeError, MessageReceiver, None, JSONMessageFormat(), DefaultEndpointService())
    
    def test_try_create_instance_with_none_format(self):
        self.assertRaises(RuntimeError, MessageReceiver, EndpointAddress("TCP", "192.168.1.2", 5050), None, DefaultEndpointService())
    
    def test_try_create_instance_with_invalid_type_of_address(self):
        self.assertRaises(TypeError, MessageReceiver, ("TCP", "192.168.1.2", 5050), JSONMessageFormat(), DefaultEndpointService())
        
    def test_try_create_instance_with_invalid_type_of_format(self):
        self.assertRaises(TypeError, MessageReceiver, EndpointAddress("TCP", "192.168.1.2", 5050), "format", DefaultEndpointService())
    
    def test_try_create_instance_with_none_service(self):
        self.assertRaises(RuntimeError, MessageReceiver, EndpointAddress("TCP", "192.168.1.2", 5050), JSONMessageFormat(), None)
    
    def test_try_create_instance_with_invalid_type_of_service(self):
        self.assertRaises(TypeError, MessageReceiver, EndpointAddress("TCP", "192.168.1.2", 5050), JSONMessageFormat(), "endpoint")
        
    def test_receive_message_with_tcp_ip_port(self):
        service = DefaultEndpointService()
        receiver = MessageReceiver(EndpointAddress("TCP", "127.0.0.1", 5050), JSONMessageFormat(), service)
        service.initialize(Communication())
        listener = MessageReceiverTest.EndpointListenerForTest()
        service.addEndpointListener(EndpointAddress("TCP", "127.0.0.1", 5050).toURI(), listener)
        
        receiver.receiveMessage(json.write({"origin":"TCP://127.0.0.1:5050","destination":"TCP://127.0.0.1:5050"}))
        self.assertTrue(listener._message)
        self.assertEquals("TCP://127.0.0.1:5050", listener._message.getOrigin().toURI())
        self.assertEquals("TCP://127.0.0.1:5050", listener._message.getDestination().toURI())
        
    def test_receive_message_with_udp_ip_port(self):
        service = DefaultEndpointService()
        receiver = MessageReceiver(EndpointAddress("UDP", "127.0.0.1", 5050), JSONMessageFormat(), service)
        service.initialize(Communication())
        listener = MessageReceiverTest.EndpointListenerForTest()
        service.addEndpointListener(EndpointAddress("UDP", "127.0.0.1", 5050).toURI(), listener)
        
        receiver.receiveMessage(json.write({"origin":"UDP://127.0.0.1:5050","destination":"UDP://127.0.0.1:5050"}))
        self.assertTrue(listener._message)
        self.assertEquals("UDP://127.0.0.1:5050", listener._message.getOrigin().toURI())
        self.assertEquals("UDP://127.0.0.1:5050", listener._message.getDestination().toURI())
        
    def test_receive_message_with_tcp_ip_port_service(self):
        service = DefaultEndpointService()
        receiver = MessageReceiver(EndpointAddress("TCP", "127.0.0.1", 5050, "service_name"), JSONMessageFormat(), service)
        service.initialize(Communication())
        listener = MessageReceiverTest.EndpointListenerForTest()
        service.addEndpointListener(EndpointAddress("TCP", "127.0.0.1", 5050, "service_name").toURI(), listener)
        
        receiver.receiveMessage(json.write({"origin":"TCP://127.0.0.1:5050/service_name","destination":"TCP://127.0.0.1:5050/service_name"}))
        self.assertTrue(listener._message)
        self.assertEquals("TCP://127.0.0.1:5050/service_name", listener._message.getOrigin().toURI())
        self.assertEquals("TCP://127.0.0.1:5050/service_name", listener._message.getDestination().toURI())
    
    def test_receive_message_with_udp_ip_port_service(self):
        service = DefaultEndpointService()
        receiver = MessageReceiver(EndpointAddress("UDP", "127.0.0.1", 5050, "service_name"), JSONMessageFormat(), service)
        service.initialize(Communication())
        listener = MessageReceiverTest.EndpointListenerForTest()
        service.addEndpointListener(EndpointAddress("UDP", "127.0.0.1", 5050, "service_name").toURI(), listener)
        
        receiver.receiveMessage(json.write({"origin":"UDP://127.0.0.1:5050/service_name","destination":"UDP://127.0.0.1:5050/service_name"}))
        self.assertTrue(listener._message)
        self.assertEquals("UDP://127.0.0.1:5050/service_name", listener._message.getOrigin().toURI())
        self.assertEquals("UDP://127.0.0.1:5050/service_name", listener._message.getDestination().toURI())
        
    class EndpointListenerForTest(EndpointListener):
        
        def __init__(self):
            self._message = None
            
        def processMessage(self, message):
            self._message = message

Microkernel().stop()