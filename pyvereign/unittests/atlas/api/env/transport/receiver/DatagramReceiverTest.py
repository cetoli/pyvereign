from atlas.api.env.transport.receiver.DatagramReceiver import DatagramReceiver
from atlas.api.env.transport.address.IPv4Address import IPv4Address
from atlas.api.env.networking.DefaultProtocol import DefaultProtocol
from atlas.api.env.transport.address.BindIPv4Address import BindIPv4Address
from atlas.api.exception.TransportError import TransportError
from atlas.api.env.transport.address.BroadcastIPv4Address import BroadcastIPv4Address
import unittest

class DatagramReceiverTest(unittest.TestCase):
    
    def test_create_instance_with_IPv4Address(self):
        self.assertTrue(DatagramReceiver(IPv4Address("192.168.1.2", 5050), DefaultProtocol()))
        print "passou"
        
    def test_create_instance_with_BindIPv4Address(self):
        self.assertTrue(DatagramReceiver(BindIPv4Address(5050), DefaultProtocol()))
        print "passou"
        
    def test_try_create_instance_with_BroadcastIPv4Address(self):
        self.assertRaises(TransportError, DatagramReceiver, BroadcastIPv4Address(5050), DefaultProtocol())
        print "passou"
        
    def test_open_receiver(self):
        receiver = DatagramReceiver(BindIPv4Address(5050), DefaultProtocol())
        self.assertTrue(receiver.open())
        self.assertTrue(receiver.close())
        
    def test_bind_receiver(self):
        receiver = DatagramReceiver(BindIPv4Address(5051), DefaultProtocol())
        self.assertTrue(receiver.open())
        self.assertTrue(receiver.bind())
        self.assertTrue(receiver.close())