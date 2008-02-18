from atlas.api.com.endpoint.address.EndpointAddress import EndpointAddress
import unittest
from atlas.api.com.endpoint.message.EndpointMessage import EndpointMessage 

class EndpointMessageTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(EndpointMessage(EndpointAddress("TCP", "192.168.1.10", 5050), EndpointAddress("TCP", "192.168.1.8", 5050)))
    
    def test_try_create_instance_with_none_origin(self):
        self.assertRaises(RuntimeError, EndpointMessage, None, EndpointAddress("TCP", "192.168.1.8", 5050))
        
    def test_try_create_instance_with_none_destination(self):
        self.assertRaises(RuntimeError, EndpointMessage, EndpointAddress("TCP", "192.168.1.8", 5050), None)
        
    def test_try_create_instance_with_invalid_type_fo_origin_parameter(self):
        self.assertRaises(TypeError, EndpointMessage, ("TCP", "192.168.1.8", 5050), EndpointAddress("TCP", "192.168.1.10", 5050))
    
    def test_try_create_instance_with_invalid_type_fo_destination_parameter(self):
        self.assertRaises(TypeError, EndpointMessage, EndpointAddress("TCP", "192.168.1.8", 5050), ("TCP", "192.168.1.10", 5050))
        
    def test_getValues(self):
        message = EndpointMessage(EndpointAddress("TCP", "192.168.1.10", 5050), EndpointAddress("TCP", "192.168.1.8", 5050))
        self.assertTrue(message.getValues())
        values = message.getValues()
        self.assertEquals(message.getOrigin().toURI(), values["origin"])
        self.assertEquals(message.getDestination().toURI(), values["destination"])
        
    