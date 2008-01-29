from atlas.api.env.transport.communicationapi.DatagramSocketAdapter import DatagramSocketAdapter
from atlas.api.env.transport.communicationapi.IPv4Address import IPv4Address
from atlas.api.env.transport.communicationapi.BindIPv4Address import BindIPv4Address
from atlas.api.env.transport.communicationapi.BroadcastIPv4Address import BroadcastIPv4Address
import unittest

class DatagramSocketAdapterTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertTrue(DatagramSocketAdapter(IPv4Address("192.168.0.12", 5000)))
    
    def test_open_and_close_adapter(self):
        adapter = DatagramSocketAdapter(IPv4Address("192.168.0.12", 5000))
        self.assertTrue(adapter.close())

    def test_support_broadcasting_true(self):
        adapter = DatagramSocketAdapter(IPv4Address("192.168.0.12", 5000))
        self.assertTrue(adapter.supportBroadcasting(True))
        self.assertTrue(adapter.isSupportingBroadcasting())
        self.assertTrue(adapter.close())
        
    def test_support_broadcasting_false(self):
        adapter = DatagramSocketAdapter(IPv4Address("192.168.0.12", 5000))
        self.assertFalse(adapter.supportBroadcasting(False))
        self.assertFalse(adapter.isSupportingBroadcasting())
        self.assertTrue(adapter.close())
    
    def test_reuse_address_true(self):
        adapter = DatagramSocketAdapter(IPv4Address("192.168.0.12", 5000))
        self.assertTrue(adapter.reuseAddress(True))
        self.assertTrue(adapter.isReusingAddress())
        self.assertTrue(adapter.close())
    
    def test_reuse_address_false(self):
        adapter = DatagramSocketAdapter(IPv4Address("192.168.0.12", 5000))
        self.assertFalse(adapter.reuseAddress(False))
        self.assertFalse(adapter.isReusingAddress())
        self.assertTrue(adapter.close())
    
    def test_send_stream_in_unicast_mode_to_bindaddress(self):
        adapter = DatagramSocketAdapter(BindIPv4Address(5050))
        self.assertEquals("test", adapter.send("test"))
        self.assertTrue(adapter.close())
        
    
    def test_send_stream_in_unicast_mode_to_ipv4_address(self):
        adapter = DatagramSocketAdapter(IPv4Address("192.168.1.2",5050))
        self.assertEquals("test", adapter.send("test"))
        self.assertTrue(adapter.close())
        
    def test_send_stream_in_unicast_mode_to_broadcast_ipv4_address(self):
        adapter = DatagramSocketAdapter(BroadcastIPv4Address(5050))
        self.assertTrue(adapter.supportBroadcasting(True))
        self.assertEquals("test", adapter.send("test"))
        self.assertTrue(adapter.close())