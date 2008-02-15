from atlas.api.com.endpoint.address.EndpointAddress import EndpointAddress
from atlas.api.exception.EndpointAddressError import EndpointAddressError
import unittest

class EndpointAddressTest(unittest.TestCase):
    
    def test_create_instance_with_tcp_ip_port(self):
        self.assertTrue(EndpointAddress("TCP", "192.168.1.2", 5050))
        
    def test_create_instance_with_udp_ip_port(self):
        self.assertTrue(EndpointAddress("UDP", "192.168.1.2", 5050))
    
    def test_create_instance_with_non_existent_protocol_ip_port(self):
        self.assertRaises(EndpointAddressError, EndpointAddress, "XXX", "192.168.1.2", 5050)
    
    def test_to_uri_with_tcp_ip_port(self):
        self.assertEquals("TCP://192.168.1.2:5050", EndpointAddress("TCP", "192.168.1.2", 5050).toURI())
        
    def test_to_uri_with_instance_with_udp_ip_port(self):
        self.assertEquals("UDP://192.168.1.2:5050", EndpointAddress("UDP", "192.168.1.2", 5050).toURI())
        
    def test_create_instance_with_tcp_ip_port_service(self):
        self.assertTrue(EndpointAddress("TCP", "192.168.1.2", 5050, "test_service"))
        
    def test_create_instance_with_udp_ip_port_service(self):
        self.assertTrue(EndpointAddress("UDP", "192.168.1.2", 5050, "test_service"))
        
    def test_to_uri_with_tcp_ip_port_service(self):
        self.assertEquals("TCP://192.168.1.2:5050/test_service", EndpointAddress("TCP", "192.168.1.2", 5050, "test_service").toURI())
        
    def test_to_uri_with_instance_with_udp_ip_port_service(self):
        self.assertEquals("UDP://192.168.1.2:5050/test_service", EndpointAddress("UDP", "192.168.1.2", 5050, "test_service").toURI())
        
    def test_create_instance_with_tcp_ip_port_service_parameters(self):
        self.assertTrue(EndpointAddress("TCP", "192.168.1.2", 5050, "test_service", "1"))
        
    def test_create_instance_with_udp_ip_port_service_parameters(self):
        self.assertTrue(EndpointAddress("UDP", "192.168.1.2", 5050, "test_service", "1"))
        
    def test_to_uri_with_tcp_ip_port_service_parameters(self):
        self.assertEquals("TCP://192.168.1.2:5050/test_service/1", EndpointAddress("TCP", "192.168.1.2", 5050, "test_service", "1").toURI())
        
    def test_to_uri_with_instance_with_udp_ip_port_service_parameters(self):
        self.assertEquals("UDP://192.168.1.2:5050/test_service/1", EndpointAddress("UDP", "192.168.1.2", 5050, "test_service", "1").toURI())
    
    def test_to_endpoint_address_with_tcp_ip_port(self):
        address = EndpointAddress.toEndpointAddress("TCP://192.168.1.2:5050")
        self.assertEquals("TCP", address.getProtocol())
        self.assertEquals("192.168.1.2", address.getIPAddress())
        self.assertEquals(5050, address.getPort())
        
    def test_to_endpoint_address_with_udp_ip_port(self):
        address = EndpointAddress.toEndpointAddress("UDP://192.168.1.2:5050")
        self.assertEquals("UDP", address.getProtocol())
        self.assertEquals("192.168.1.2", address.getIPAddress())
        self.assertEquals(5050, address.getPort())
        
    def test_to_endpoint_address_with_tcp_ip_port_service(self):
        address = EndpointAddress.toEndpointAddress("TCP://192.168.1.2:5050/service")
        self.assertEquals("TCP", address.getProtocol())
        self.assertEquals("192.168.1.2", address.getIPAddress())
        self.assertEquals(5050, address.getPort())
        self.assertEquals("service", address.getService())
        
    def test_to_endpoint_address_with_udp_ip_port_service(self):
        address = EndpointAddress.toEndpointAddress("UDP://192.168.1.2:5050/service")
        self.assertEquals("UDP", address.getProtocol())
        self.assertEquals("192.168.1.2", address.getIPAddress())
        self.assertEquals(5050, address.getPort())
        self.assertEquals("service", address.getService())
    
    def test_to_endpoint_address_with_tcp_ip_port_service_parameters(self):
        address = EndpointAddress.toEndpointAddress("TCP://192.168.1.2:5050/service/1")
        self.assertEquals("TCP", address.getProtocol())
        self.assertEquals("192.168.1.2", address.getIPAddress())
        self.assertEquals(5050, address.getPort())
        self.assertEquals("service", address.getService())
        self.assertEquals("1", address.getParameters())
        
    def test_to_endpoint_address_with_udp_ip_port_service_parameters(self):
        address = EndpointAddress.toEndpointAddress("UDP://192.168.1.2:5050/service/1")
        self.assertEquals("UDP", address.getProtocol())
        self.assertEquals("192.168.1.2", address.getIPAddress())
        self.assertEquals(5050, address.getPort())
        self.assertEquals("service", address.getService())    
        self.assertEquals("1", address.getParameters())
    
    