from org.pyvereign.core.communication.endpoint.address.EndpointAddress import EndpointAddress
import unittest

class EndpointAddressTest(unittest.TestCase):
    
    def test_try_create_instance_with_none_protocol(self):
        self.assertRaises(TypeError, EndpointAddress, None, "192.168.1.2", 5050, "service", "action")
    
    def test_try_create_instance_with_none_ipaddress(self):
        self.assertRaises(TypeError, EndpointAddress, "TCP", None, 5050, "service", "action")
        
    def test_try_create_instance_with_negative_port(self):
        self.assertRaises(RuntimeError, EndpointAddress, "TCP", "192.168.0.1", -5050, "service", "action")
        
    def test_try_create_instance_with_zero_value_for_port(self):
        self.assertRaises(RuntimeError, EndpointAddress, "TCP", "192.168.0.1", 0, "service", "action")
        
    def test_try_create_instance_with_none_port(self):
        self.assertRaises(TypeError, EndpointAddress, "TCP", "192.168.1.2", None, "service", "action")
        
    def test_try_create_instance_with_none_service(self):
        self.assertRaises(TypeError, EndpointAddress, "TCP", "192.168.1.2", 5050, None, "action")
    
    def test_try_create_instance_with_none_action(self):
        self.assertRaises(TypeError, EndpointAddress, "TCP", "192.168.1.2", 5050, "service", None)
        
    def test_try_create_instance_with_invalid_type_for_protocol(self):
        self.assertRaises(TypeError, EndpointAddress, 12, "192.168.1.2", 5050,"service", "12")
        
    def test_try_create_instance_with_invalid_type_for_action(self):
        self.assertRaises(TypeError, EndpointAddress, "TCP", "192.168.1.2", 5050, "service", 12)
        
    def test_try_create_instance_with_invalid_type_for_ipaddress(self):
        self.assertRaises(TypeError, EndpointAddress, "TCP", 192.168, 5050,"service", "12")
        
    def test_try_create_instance_with_invalid_type_for_port(self):
        self.assertRaises(TypeError, EndpointAddress, "TCP", "192.168.1.2", "5050", "service", "12")
        
    def test_try_create_instance_with_invalid_type_for_service(self):
        self.assertRaises(TypeError, EndpointAddress, "TCP", "192.168.1.2", 5050, 123, "12")
    
    def test_create_instance_with_tcp_ip_port_service_action(self):
        self.assertTrue(EndpointAddress("TCP", "192.168.1.2", 5050, "test_service", "action"))
        address = EndpointAddress("TCP", "192.168.1.2", 5050, "test_service", "action")
        self.assertEquals("TCP://192.168.1.2:5050/test_service/action", address.toURI())
        
    def test_create_instance_with_udp_ip_port_service_action(self):
        self.assertTrue(EndpointAddress("UDP", "192.168.1.2", 5050, "test_service", "action"))
        address = EndpointAddress("UDP", "192.168.1.2", 5050, "test_service", "action")
        self.assertEquals("UDP://192.168.1.2:5050/test_service/action", address.toURI())
        
    def test_create_instance_with_tcp_ip_port_service(self):
        self.assertTrue(EndpointAddress("TCP", "192.168.1.2", 5050, "test_service"))
        address = EndpointAddress("TCP", "192.168.1.2", 5050, "test_service")
        self.assertEquals("TCP://192.168.1.2:5050/test_service", address.toURI())
    
    def test_create_instance_with_udp_ip_port_service(self):
        self.assertTrue(EndpointAddress("UDP", "192.168.1.2", 5050, "test_service"))
        address = EndpointAddress("UDP", "192.168.1.2", 5050, "test_service")
        self.assertEquals("UDP://192.168.1.2:5050/test_service", address.toURI())
        
    def test_create_instance_with_tcp_ip_port_service_action_parameter(self):
        self.assertTrue(EndpointAddress("TCP", "192.168.1.2", 5050, "test_service", "action", "1"))
        address = EndpointAddress("TCP", "192.168.1.2", 5050, "test_service", "action", "1")
        self.assertEquals("TCP://192.168.1.2:5050/test_service/action/1", address.toURI())
    
    def test_create_instance_with_udp_ip_port_service_action_parameter(self):
        self.assertTrue(EndpointAddress("UDP", "192.168.1.2", 5050, "test_service", "action", "1"))
        address = EndpointAddress("UDP", "192.168.1.2", 5050, "test_service", "action", "1")
        self.assertEquals("UDP://192.168.1.2:5050/test_service/action/1", address.toURI())
    
    def test_get_endpoint_address_tcp_ip_port_service(self):
        self.assertTrue(EndpointAddress.getEndpointAddress("TCP://192.168.1.2:5050/test_service/"))
        address = EndpointAddress.getEndpointAddress("TCP://192.168.1.2:5050/test_service/")
        
        self.assertEquals("TCP", address.getProtocol())
        self.assertEquals("192.168.1.2", address.getIPAddress())
        self.assertEquals(5050, address.getPort())
        self.assertEquals("test_service", address.getService())
    
    def test_get_endpoint_address_udp_ip_port_service(self):
        self.assertTrue(EndpointAddress.getEndpointAddress("UDP://192.168.1.2:5050/test_service/"))
        address = EndpointAddress.getEndpointAddress("UDP://192.168.1.2:5050/test_service/")
        
        self.assertEquals("UDP", address.getProtocol())
        self.assertEquals("192.168.1.2", address.getIPAddress())
        self.assertEquals(5050, address.getPort())
        self.assertEquals("test_service", address.getService())
        
    def test_get_endpoint_address_tcp_ip_port_service_action(self):
        self.assertTrue(EndpointAddress.getEndpointAddress("TCP://192.168.1.2:5050/test_service/action"))
        address = EndpointAddress.getEndpointAddress("TCP://192.168.1.2:5050/test_service/action")
        
        self.assertEquals("TCP", address.getProtocol())
        self.assertEquals("192.168.1.2", address.getIPAddress())
        self.assertEquals(5050, address.getPort())
        self.assertEquals("test_service", address.getService())
        self.assertEquals("action", address.getAction())
    
    def test_get_endpoint_address_udp_ip_port_service_action(self):
        self.assertTrue(EndpointAddress.getEndpointAddress("UDP://192.168.1.2:5050/test_service/action"))
        address = EndpointAddress.getEndpointAddress("UDP://192.168.1.2:5050/test_service/action")
        
        self.assertEquals("UDP", address.getProtocol())
        self.assertEquals("192.168.1.2", address.getIPAddress())
        self.assertEquals(5050, address.getPort())
        self.assertEquals("test_service", address.getService())
        self.assertEquals("action", address.getAction())
    
    def test_get_endpoint_address_tcp_ip_port_service_action_parameter(self):
        self.assertTrue(EndpointAddress.getEndpointAddress("TCP://192.168.1.2:5050/test_service/action/parameter"))
        address = EndpointAddress.getEndpointAddress("TCP://192.168.1.2:5050/test_service/action/parameter")
        
        self.assertEquals("TCP", address.getProtocol())
        self.assertEquals("192.168.1.2", address.getIPAddress())
        self.assertEquals(5050, address.getPort())
        self.assertEquals("test_service", address.getService())
        self.assertEquals("action", address.getAction())
        self.assertEquals("parameter", address.getParameter())
    
    def test_get_endpoint_address_udp_ip_port_service_action_parameter(self):
        self.assertTrue(EndpointAddress.getEndpointAddress("UDP://192.168.1.2:5050/test_service/action/parameter"))
        address = EndpointAddress.getEndpointAddress("UDP://192.168.1.2:5050/test_service/action/parameter")
        
        self.assertEquals("UDP", address.getProtocol())
        self.assertEquals("192.168.1.2", address.getIPAddress())
        self.assertEquals(5050, address.getPort())
        self.assertEquals("test_service", address.getService())
        self.assertEquals("action", address.getAction())
        self.assertEquals("parameter", address.getParameter())
    
    def test_try_get_endpoint_address_with_none_uri(self):
        self.assertRaises(RuntimeError, EndpointAddress.getEndpointAddress, None)
        
        