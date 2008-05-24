from org.pyvereign.core.communication.format.JSONFormat import JSONFormat
from org.pyvereign.core.communication.endpoint.address.EndpointAddress import EndpointAddress
from org.pyvereign.core.communication.endpoint.message.EndpointMessage import EndpointMessage
from org.pyvereign.core.exception.FormatError import FormatError
import unittest

class JSONFormatTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(JSONFormat())
        
    def test_marshal_endpoint_message(self):
        message = EndpointMessage(EndpointAddress("TCP", "192.168.1.10", 5050), EndpointAddress("TCP", "192.168.1.8", 5050))
        format = JSONFormat()
        self.assertTrue(format.marshal(message))
        self.assertTrue(format.marshal(message).find("origin") >= 0)
        self.assertTrue(format.marshal(message).find("destination") >= 0)
        self.assertTrue(format.marshal(message).find("class") >= 0)
        self.assertTrue(format.marshal(message).find("module") >= 0)        
    
    def test_unmarshal_endpoint_message(self):
        message = EndpointMessage(EndpointAddress("TCP", "192.168.1.10", 5050), EndpointAddress("TCP", "192.168.1.8", 5050))
        format = JSONFormat()
        self.assertTrue(format.unmarshal(format.marshal(message)))
        msg = format.unmarshal(format.marshal(message))
        self.assertEquals(message.getOrigin().toURI(), msg.getOrigin().toURI())
        self.assertEquals(message.getDestination().toURI(), msg.getDestination().toURI())
        
    def test_try_marshal_an_non_formatable_object(self):
        self.assertRaises(TypeError, JSONFormat().marshal, "test")
    
    def test_try_marshal_an_none_formatable_object(self):
        self.assertRaises(TypeError, JSONFormat().marshal, None)
    
    def test_try_unmarshal_none_stream(self):
        self.assertRaises(TypeError, JSONFormat().unmarshal, None)
        
    def test_try_unmarshal_non_stream(self):
        self.assertRaises(TypeError, JSONFormat().unmarshal, 123)
        
    def test_try_unmarshal_invalid_stream(self):
        self.assertRaises(FormatError, JSONFormat().unmarshal, "{}")
    
