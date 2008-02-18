from atlas.api.com.endpoint.format.JSONMessageFormat import JSONMessageFormat
from atlas.api.com.endpoint.message.EndpointMessage import EndpointMessage
from atlas.api.com.endpoint.address.EndpointAddress import EndpointAddress
import unittest

class JSONMessageFormatTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(JSONMessageFormat())
        
    def test_marshal_message(self):
        format = JSONMessageFormat()
        message = EndpointMessage(EndpointAddress("TCP", "192.168.1.10", 5050), EndpointAddress("TCP", "192.168.1.8", 5050))
        self.assertTrue(len(format.marshal(message)))
        
    def test_unmarshal_message(self):
        format = JSONMessageFormat()
        message = EndpointMessage(EndpointAddress("TCP", "192.168.1.10", 5050), EndpointAddress("TCP", "192.168.1.8", 5050))
        stream = format.marshal(message)
        
        self.assertTrue(format.unmarshal(stream))
        self.assertEquals(EndpointMessage, format.unmarshal(stream).__class__)
        
        m = format.unmarshal(stream)
        
        self.assertEquals("TCP://192.168.1.10:5050", m.getOrigin().toURI())
        self.assertEquals("TCP://192.168.1.8:5050", m.getDestination().toURI())