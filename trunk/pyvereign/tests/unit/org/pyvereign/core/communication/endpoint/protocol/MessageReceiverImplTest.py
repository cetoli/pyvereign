from org.pyvereign.core.communication.endpoint.protocol.MessageReceiverImpl import MessageReceiverImpl
from org.pyvereign.core.communication.endpoint.address.EndpointAddress import EndpointAddress
from org.pyvereign.core.microkernel.Microkernel import Microkernel
from org.pyvereign.core.communication.endpoint.listener.EndpointListener import EndpointListener
from org.pyvereign.core.id.IDFactory import IDFactory
from org.pyvereign.util.Constants import Constants
from org.pyvereign.core.communication.endpoint.message.EndpointMessage import EndpointMessage
from org.pyvereign.core.communication.format.JSONFormat import JSONFormat
import unittest

class MessageReceiverImplTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(MessageReceiverImpl(EndpointAddress("TCP", "192.168.1.2", 5050), Microkernel()))
    
    def test_try_create_instance_with_none_endpointaddress(self):
        self.assertRaises(TypeError, MessageReceiverImpl, None, Microkernel())
        
    def test_try_create_instance_with_none_microkernel(self):
        self.assertRaises(TypeError, MessageReceiverImpl, EndpointAddress("TCP", "192.168.1.2", 5050), None)
    
    def test_try_create_instance_with_invalid_type_for_endpointaddress(self):
        self.assertRaises(TypeError, MessageReceiverImpl, ("TCP", "192.168.1.2", 5050), Microkernel())
    
    def test_try_create_instance_with_invalid_type_for_microkernel(self):
        self.assertRaises(TypeError, MessageReceiverImpl, EndpointAddress("TCP", "192.168.1.2", 5050), "atlas")
    
    def test_receive_message_with_tcp_ip_port(self):
        kernel = Microkernel()
        self.assertEquals(Microkernel.NON_INITIALIZED, kernel.getStatus())
        kernel.initialize()
        self.assertEquals(Microkernel.INITIALIZED, kernel.getStatus())
        receiver = MessageReceiverImpl(EndpointAddress("TCP", "127.0.0.1", 5050), kernel)
        self.assertTrue(kernel.hasModule(IDFactory().createInternalServerID(Constants.COMMUNICATION)))
        self.assertTrue(kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION)))
        communication = kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION))
        communication.addEndpointListener(EndpointAddress("TCP", "127.0.0.1", 5050).toURI(), EndpointListenerForTest())
        message = EndpointMessage(EndpointAddress("TCP", "127.0.0.1", 5050), EndpointAddress("TCP", "127.0.0.1", 5050), None)
        stream = JSONFormat().marshal(message)
        self.assertTrue(receiver.receiveMessage(stream))
        msg = receiver.receiveMessage(stream)
        self.assertEquals(EndpointAddress("TCP", "127.0.0.1", 5050).toURI(), msg.getOrigin().toURI())
        self.assertEquals(EndpointAddress("TCP", "127.0.0.1", 5050).toURI(), msg.getDestination().toURI())
    
    def test_receive_message_with_tcp_ip_port_service(self):
        kernel = Microkernel()
        self.assertEquals(Microkernel.NON_INITIALIZED, kernel.getStatus())
        kernel.initialize()
        self.assertEquals(Microkernel.INITIALIZED, kernel.getStatus())
        receiver = MessageReceiverImpl(EndpointAddress("TCP", "127.0.0.1", 5050, "service"), kernel)
        self.assertTrue(kernel.hasModule(IDFactory().createInternalServerID(Constants.COMMUNICATION)))
        self.assertTrue(kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION)))
        communication = kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION))
        communication.addEndpointListener(EndpointAddress("TCP", "127.0.0.1", 5050, "service").toURI(), EndpointListenerForTest())
        message = EndpointMessage(EndpointAddress("TCP", "127.0.0.1", 5050, "service"), EndpointAddress("TCP", "127.0.0.1", 5050, "service"), None)
        stream = JSONFormat().marshal(message)
        self.assertTrue(receiver.receiveMessage(stream))
        msg = receiver.receiveMessage(stream)
        self.assertEquals(EndpointAddress("TCP", "127.0.0.1", 5050, "service").toURI(), msg.getOrigin().toURI())
        self.assertEquals(EndpointAddress("TCP", "127.0.0.1", 5050, "service").toURI(), msg.getDestination().toURI())
    
    def test_receive_message_with_tcp_ip_port_service_action(self):
        kernel = Microkernel()
        self.assertEquals(Microkernel.NON_INITIALIZED, kernel.getStatus())
        kernel.initialize()
        self.assertEquals(Microkernel.INITIALIZED, kernel.getStatus())
        receiver = MessageReceiverImpl(EndpointAddress("TCP", "127.0.0.1", 5050, "service", "action"), kernel)
        self.assertTrue(kernel.hasModule(IDFactory().createInternalServerID(Constants.COMMUNICATION)))
        self.assertTrue(kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION)))
        communication = kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION))
        communication.addEndpointListener(EndpointAddress("TCP", "127.0.0.1", 5050, "service", "action").toURI(), EndpointListenerForTest())
        message = EndpointMessage(EndpointAddress("TCP", "127.0.0.1", 5050, "service", "action"), EndpointAddress("TCP", "127.0.0.1", 5050, "service", "action"), None)
        stream = JSONFormat().marshal(message)
        self.assertTrue(receiver.receiveMessage(stream))
        msg = receiver.receiveMessage(stream)
        self.assertEquals(EndpointAddress("TCP", "127.0.0.1", 5050, "service", "action").toURI(), msg.getOrigin().toURI())
        self.assertEquals(EndpointAddress("TCP", "127.0.0.1", 5050, "service", "action").toURI(), msg.getDestination().toURI())
    
    def test_receive_message_with_tcp_ip_port_service_action_parameter(self):
        kernel = Microkernel()
        self.assertEquals(Microkernel.NON_INITIALIZED, kernel.getStatus())
        kernel.initialize()
        self.assertEquals(Microkernel.INITIALIZED, kernel.getStatus())
        receiver = MessageReceiverImpl(EndpointAddress("TCP", "127.0.0.1", 5050, "service", "action", "parameter"), kernel)
        self.assertTrue(kernel.hasModule(IDFactory().createInternalServerID(Constants.COMMUNICATION)))
        self.assertTrue(kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION)))
        communication = kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION))
        communication.addEndpointListener(EndpointAddress("TCP", "127.0.0.1", 5050, "service", "action", "parameter").toURI(), EndpointListenerForTest())
        message = EndpointMessage(EndpointAddress("TCP", "127.0.0.1", 5050, "service", "action", "parameter"), EndpointAddress("TCP", "127.0.0.1", 5050, "service", "action", "parameter"), None)
        stream = JSONFormat().marshal(message)
        self.assertTrue(receiver.receiveMessage(stream))
        msg = receiver.receiveMessage(stream)
        self.assertEquals(EndpointAddress("TCP", "127.0.0.1", 5050, "service", "action", "parameter").toURI(), msg.getOrigin().toURI())
        self.assertEquals(EndpointAddress("TCP", "127.0.0.1", 5050, "service", "action", "parameter").toURI(), msg.getDestination().toURI())
    
    def test_receive_message_with_udp_ip_port(self):
        kernel = Microkernel()
        self.assertEquals(Microkernel.NON_INITIALIZED, kernel.getStatus())
        kernel.initialize()
        self.assertEquals(Microkernel.INITIALIZED, kernel.getStatus())
        receiver = MessageReceiverImpl(EndpointAddress("UDP", "127.0.0.1", 5050), kernel)
        self.assertTrue(kernel.hasModule(IDFactory().createInternalServerID(Constants.COMMUNICATION)))
        self.assertTrue(kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION)))
        communication = kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION))
        communication.addEndpointListener(EndpointAddress("UDP", "127.0.0.1", 5050).toURI(), EndpointListenerForTest())
        message = EndpointMessage(EndpointAddress("UDP", "127.0.0.1", 5050), EndpointAddress("UDP", "127.0.0.1", 5050), None)
        stream = JSONFormat().marshal(message)
        self.assertTrue(receiver.receiveMessage(stream))
        msg = receiver.receiveMessage(stream)
        self.assertEquals(EndpointAddress("UDP", "127.0.0.1", 5050).toURI(), msg.getOrigin().toURI())
        self.assertEquals(EndpointAddress("UDP", "127.0.0.1", 5050).toURI(), msg.getDestination().toURI())
    
    def test_receive_message_with_udp_ip_port_service(self):
        kernel = Microkernel()
        self.assertEquals(Microkernel.NON_INITIALIZED, kernel.getStatus())
        kernel.initialize()
        self.assertEquals(Microkernel.INITIALIZED, kernel.getStatus())
        receiver = MessageReceiverImpl(EndpointAddress("UDP", "127.0.0.1", 5050, "service"), kernel)
        self.assertTrue(kernel.hasModule(IDFactory().createInternalServerID(Constants.COMMUNICATION)))
        self.assertTrue(kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION)))
        communication = kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION))
        communication.addEndpointListener(EndpointAddress("UDP", "127.0.0.1", 5050, "service").toURI(), EndpointListenerForTest())
        message = EndpointMessage(EndpointAddress("UDP", "127.0.0.1", 5050, "service"), EndpointAddress("UDP", "127.0.0.1", 5050, "service"), None)
        stream = JSONFormat().marshal(message)
        self.assertTrue(receiver.receiveMessage(stream))
        msg = receiver.receiveMessage(stream)
        self.assertEquals(EndpointAddress("UDP", "127.0.0.1", 5050, "service").toURI(), msg.getOrigin().toURI())
        self.assertEquals(EndpointAddress("UDP", "127.0.0.1", 5050, "service").toURI(), msg.getDestination().toURI())
    
    def test_receive_message_with_udp_ip_port_service_action(self):
        kernel = Microkernel()
        self.assertEquals(Microkernel.NON_INITIALIZED, kernel.getStatus())
        kernel.initialize()
        self.assertEquals(Microkernel.INITIALIZED, kernel.getStatus())
        receiver = MessageReceiverImpl(EndpointAddress("UDP", "127.0.0.1", 5050, "service", "action"), kernel)
        self.assertTrue(kernel.hasModule(IDFactory().createInternalServerID(Constants.COMMUNICATION)))
        self.assertTrue(kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION)))
        communication = kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION))
        communication.addEndpointListener(EndpointAddress("UDP", "127.0.0.1", 5050, "service", "action").toURI(), EndpointListenerForTest())
        message = EndpointMessage(EndpointAddress("UDP", "127.0.0.1", 5050, "service", "action"), EndpointAddress("UDP", "127.0.0.1", 5050, "service", "action"), None)
        stream = JSONFormat().marshal(message)
        self.assertTrue(receiver.receiveMessage(stream))
        msg = receiver.receiveMessage(stream)
        self.assertEquals(EndpointAddress("UDP", "127.0.0.1", 5050, "service", "action").toURI(), msg.getOrigin().toURI())
        self.assertEquals(EndpointAddress("UDP", "127.0.0.1", 5050, "service", "action").toURI(), msg.getDestination().toURI())
    
    def test_receive_message_with_udp_ip_port_service_action_parameter(self):
        kernel = Microkernel()
        self.assertEquals(Microkernel.NON_INITIALIZED, kernel.getStatus())
        kernel.initialize()
        self.assertEquals(Microkernel.INITIALIZED, kernel.getStatus())
        receiver = MessageReceiverImpl(EndpointAddress("UDP", "127.0.0.1", 5050, "service", "action", "parameter"), kernel)
        self.assertTrue(kernel.hasModule(IDFactory().createInternalServerID(Constants.COMMUNICATION)))
        self.assertTrue(kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION)))
        communication = kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION))
        communication.addEndpointListener(EndpointAddress("UDP", "127.0.0.1", 5050, "service", "action", "parameter").toURI(), EndpointListenerForTest())
        message = EndpointMessage(EndpointAddress("UDP", "127.0.0.1", 5050, "service", "action", "parameter"), EndpointAddress("UDP", "127.0.0.1", 5050, "service", "action", "parameter"), None)
        stream = JSONFormat().marshal(message)
        self.assertTrue(receiver.receiveMessage(stream))
        msg = receiver.receiveMessage(stream)
        self.assertEquals(EndpointAddress("UDP", "127.0.0.1", 5050, "service", "action", "parameter").toURI(), msg.getOrigin().toURI())
        self.assertEquals(EndpointAddress("UDP", "127.0.0.1", 5050, "service", "action", "parameter").toURI(), msg.getDestination().toURI())
        
class EndpointListenerForTest(EndpointListener):
        
        def __init__(self):
            self._message = None
            
        def processMessage(self, message):
            self._message = message
        
        