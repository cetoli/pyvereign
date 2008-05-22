from org.pyvereign.core.communication.endpoint.protocol.MessageSenderImpl import MessageSenderImpl
from org.pyvereign.core.communication.endpoint.address.EndpointAddress import EndpointAddress
from org.pyvereign.core.communication.format.JSONFormat import JSONFormat
from org.pyvereign.core.microkernel.Microkernel import Microkernel
from org.pyvereign.core.communication.endpoint.message.EndpointMessage import EndpointMessage
import unittest

class MessageSenderImplTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(MessageSenderImpl(EndpointAddress("TCP", "192.168.0.12", 5050), Microkernel()))
    
    def test_try_create_instance_with_none_endpoint_address(self):
        self.assertRaises(TypeError, MessageSenderImpl, None, Microkernel())
    
    def test_try_create_instance_with_none_kernel(self):
        self.assertRaises(TypeError, MessageSenderImpl, EndpointAddress("TCP", "192.168.1.2", 5050), None)
    
    def test_try_create_instance_with_invalid_type_of_address(self):
        self.assertRaises(TypeError, MessageSenderImpl, ("TCP", "192.168.1.2", 5050), Microkernel())
        
    def test_send_message_with_tcp_ip_port(self):
        address = EndpointAddress("TCP", "127.0.0.1", 5050)
        format = JSONFormat()
        kernel = Microkernel()
        kernel.initialize()
        sender = MessageSenderImpl(address, kernel)
        message = EndpointMessage(address, address)
        
        self.assertEquals(message, sender.sendMessage(message, format))
        
    def test_send_message_with_tcp_ip_port_5052(self):
        address = EndpointAddress("TCP", "127.0.0.1", 5052)
        format = JSONFormat()
        kernel = Microkernel()
        kernel.initialize()
        sender = MessageSenderImpl(address, kernel)
        message = EndpointMessage(address, address)
        
        self.assertEquals(message, sender.sendMessage(message, format))
    
    def test_send_message_with_tcp_ip_port_service(self):
        address = EndpointAddress("TCP", "127.0.0.1", 5050, "service")
        format = JSONFormat()
        kernel = Microkernel()
        kernel.initialize()
        sender = MessageSenderImpl(address, kernel)
        message = EndpointMessage(address, address)
        
        self.assertEquals(message, sender.sendMessage(message, format))
    
    def test_send_message_with_tcp_ip_port_5052_service(self):
        address = EndpointAddress("TCP", "127.0.0.1", 5052, "service")
        format = JSONFormat()
        kernel = Microkernel()
        kernel.initialize()
        sender = MessageSenderImpl(address, kernel)
        message = EndpointMessage(address, address)
        
        self.assertEquals(message, sender.sendMessage(message, format))
        
    def test_send_message_with_tcp_ip_port_service_action(self):
        address = EndpointAddress("TCP", "127.0.0.1", 5050, "service", "action")
        format = JSONFormat()
        kernel = Microkernel()
        kernel.initialize()
        sender = MessageSenderImpl(address, kernel)
        message = EndpointMessage(address, address)
        
        self.assertEquals(message, sender.sendMessage(message, format))
    
    def test_send_message_with_tcp_ip_port_5052_service_action(self):
        address = EndpointAddress("TCP", "127.0.0.1", 5052, "service", "action")
        format = JSONFormat()
        kernel = Microkernel()
        kernel.initialize()
        sender = MessageSenderImpl(address, kernel)
        message = EndpointMessage(address, address)
        
        self.assertEquals(message, sender.sendMessage(message, format))
        
    def test_send_message_with_tcp_ip_port_service_action_parameter(self):
        address = EndpointAddress("TCP", "127.0.0.1", 5050, "service", "parameter")
        format = JSONFormat()
        kernel = Microkernel()
        kernel.initialize()
        sender = MessageSenderImpl(address, kernel)
        message = EndpointMessage(address, address)
        
        self.assertEquals(message, sender.sendMessage(message, format))
    
    def test_send_message_with_tcp_ip_port_5052_service_action_parameter(self):
        address = EndpointAddress("TCP", "127.0.0.1", 5052, "service", "parameter")
        format = JSONFormat()
        kernel = Microkernel()
        kernel.initialize()
        sender = MessageSenderImpl(address, kernel)
        message = EndpointMessage(address, address)
        
        self.assertEquals(message, sender.sendMessage(message, format))
    
    def test_send_message_with_udp_ip_port(self):
        address = EndpointAddress("UDP", "127.0.0.1", 5050)
        format = JSONFormat()
        kernel = Microkernel()
        kernel.initialize()
        sender = MessageSenderImpl(address, kernel)
        message = EndpointMessage(address, address)
        
        self.assertEquals(message, sender.sendMessage(message, format))
        
    def test_send_message_with_udp_ip_port_5052(self):
        address = EndpointAddress("UDP", "127.0.0.1", 5052)
        format = JSONFormat()
        kernel = Microkernel()
        kernel.initialize()
        sender = MessageSenderImpl(address, kernel)
        message = EndpointMessage(address, address)
        
        self.assertEquals(message, sender.sendMessage(message, format))
    
    def test_send_message_with_udp_ip_port_service(self):
        address = EndpointAddress("UDP", "127.0.0.1", 5050, "service")
        format = JSONFormat()
        kernel = Microkernel()
        kernel.initialize()
        sender = MessageSenderImpl(address, kernel)
        message = EndpointMessage(address, address)
        
        self.assertEquals(message, sender.sendMessage(message, format))
        
    def test_send_message_with_udp_ip_port_5052_service(self):
        address = EndpointAddress("UDP", "127.0.0.1", 5052, "service")
        format = JSONFormat()
        kernel = Microkernel()
        kernel.initialize()
        sender = MessageSenderImpl(address, kernel)
        message = EndpointMessage(address, address)
        
        self.assertEquals(message, sender.sendMessage(message, format))
        
    def test_send_message_with_udp_broadcast_mode(self):
        address = EndpointAddress("UDP", "<broadcast>", 5050)
        format = JSONFormat()
        kernel = Microkernel()
        kernel.initialize()
        sender = MessageSenderImpl(address, kernel)
        message = EndpointMessage(address, address)
        
        self.assertEquals(message, sender.sendMessage(message, format))
    
    def test_send_message_with_udp_broadcast_port_service(self):
        address = EndpointAddress("UDP", "<broadcast>", 5050, "service")
        format = JSONFormat()
        kernel = Microkernel()
        kernel.initialize()
        sender = MessageSenderImpl(address, kernel)
        message = EndpointMessage(address, address)
        
        self.assertEquals(message, sender.sendMessage(message, format))