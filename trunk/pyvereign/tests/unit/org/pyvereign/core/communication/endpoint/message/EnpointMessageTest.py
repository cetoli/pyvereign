from org.pyvereign.core.communication.endpoint.message.EndpointMessage import EndpointMessage
from org.pyvereign.core.communication.endpoint.address.EndpointAddress import EndpointAddress
from org.pyvereign.core.exception.FormatableObjectError import FormatableObjectError
import unittest

class EndpointMessageTest(unittest.TestCase):
    
    def test_create_instance_without_parameters(self):
        self.assertTrue(EndpointMessage())
    
    def test_create_instance_with_origin_destination(self):
        self.assertTrue(EndpointMessage(EndpointAddress("TCP", "192.168.1.10", 5050), EndpointAddress("TCP", "192.168.1.8", 5050)))
    
    def test_try_create_instance_with_invalid_type_fo_origin_parameter(self):
        self.assertRaises(TypeError, EndpointMessage, ("TCP", "192.168.1.8", 5050), EndpointAddress("TCP", "192.168.1.10", 5050))
    
    def test_try_create_instance_with_invalid_type_fo_destination_parameter(self):
        self.assertRaises(TypeError, EndpointMessage, EndpointAddress("TCP", "192.168.1.8", 5050), ("TCP", "192.168.1.10", 5050))
        
    def test_get_values(self):
        message = EndpointMessage(EndpointAddress("TCP", "192.168.1.10", 5050), EndpointAddress("TCP", "192.168.1.8", 5050))
        values = message.getValues()
        self.assertTrue(values.has_key("origin"))
        self.assertEquals("TCP://192.168.1.10:5050/", values["origin"])
        self.assertTrue(values.has_key("destination"))
        self.assertEquals("TCP://192.168.1.8:5050/", values["destination"])
        
    def test_set_values(self):
        values = {"origin": "TCP://192.168.1.10:5050/", "destination": "TCP://192.168.1.8:5050/"}
        message = EndpointMessage()
        self.assertEquals(values, message.setValues(values))
        self.assertEquals("TCP://192.168.1.10:5050/", message.getOrigin().toURI())
        self.assertEquals("TCP://192.168.1.8:5050/", message.getDestination().toURI())
        
    def test_try_set_none_values(self):
        self.assertRaises(TypeError, EndpointMessage().setValues, None)
        
    def test_try_set_invalid_type_for_values(self):
        self.assertRaises(TypeError, EndpointMessage().setValues, "{origin: fhsjfs}")
        
    def test_try_set_invalid_values(self):
        self.assertRaises(FormatableObjectError, EndpointMessage().setValues, {"destination": "TCP://192.168.1.8:5050/"})
        self.assertRaises(FormatableObjectError, EndpointMessage().setValues, {"origin": "TCP://192.168.1.8:5050/"})
        
    def test_try_get_values(self):
        self.assertRaises(FormatableObjectError, EndpointMessage().getValues)
    