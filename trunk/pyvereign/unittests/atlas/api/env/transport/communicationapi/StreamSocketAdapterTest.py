from atlas.api.env.transport.communicationapi.StreamSocketAdapter import StreamSocketAdapter
from atlas.api.env.transport.communicationapi.IPv4Address import IPv4Address
from atlas.api.env.transport.communicationapi.BindIPv4Address import BindIPv4Address
import unittest

class StreamSocketAdapterTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(StreamSocketAdapter(IPv4Address("192.168.1.10", 5050)))
        
    def test_open_and_close_stream_socket(self):
        adapter = StreamSocketAdapter(BindIPv4Address(5051))
        self.assertTrue(adapter.open())
        self.assertTrue(adapter.close())
    
    def test_support_broadcasting(self):
        adapter = StreamSocketAdapter(IPv4Address("192.168.1.10", 5050))
        self.assertRaises(RuntimeError, adapter.supportBroadcasting, True)
    
    def test_reuse_address_true(self):
        adapter1 = StreamSocketAdapter(BindIPv4Address(5050))
        self.assertTrue(adapter1.reuseAddress(True))
        self.assertTrue(adapter1.isReusingAddress())
        
        adapter2 = StreamSocketAdapter(BindIPv4Address(5050))
        self.assertTrue(adapter2.reuseAddress(True))
        self.assertTrue(adapter2.isReusingAddress())
        
        self.assertTrue(adapter1.open())
        self.assertTrue(adapter2.open())
        
        self.assertTrue(adapter1.close())
        self.assertTrue(adapter2.close())
        
    def test_reuse_address_false(self):
        adapter1 = StreamSocketAdapter(BindIPv4Address(5050))
        self.assertTrue(adapter1.reuseAddress(True))
        self.assertTrue(adapter1.isReusingAddress())
        self.assertTrue(adapter1.close())
        
    def test_send_stream_to_bind_address(self):
        adapter = StreamSocketAdapter(BindIPv4Address(5050))
        self.assertEquals("test", adapter.send("test"))
        self.assertTrue(adapter.close())
        
    def test_set_timeout(self):
        adapter = StreamSocketAdapter(IPv4Address("192.168.1.10", 5050))
        self.assertEquals(10, adapter.setTimeOut(10))
        self.assertEquals(10, adapter.getTimeOut())