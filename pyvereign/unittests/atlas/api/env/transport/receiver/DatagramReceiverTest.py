from atlas.api.env.transport.receiver.DatagramReceiver import DatagramReceiver
from atlas.api.env.transport.address.IPv4Address import IPv4Address
from atlas.api.env.networking.DefaultProtocol import DefaultProtocol
from atlas.api.env.transport.address.BindIPv4Address import BindIPv4Address
from atlas.api.exception.TransportError import TransportError
from atlas.api.env.transport.address.BroadcastIPv4Address import BroadcastIPv4Address
from atlas.api.exception.BindError import BindError
import pmock
import unittest

class DatagramReceiverTest(unittest.TestCase):
    
    def test_create_instance_with_IPv4Address(self):
        self.assertTrue(DatagramReceiver(IPv4Address("192.168.1.2", 5050), DefaultProtocol()))
        
    def test_create_instance_with_BindIPv4Address(self):
        self.assertTrue(DatagramReceiver(BindIPv4Address(5050), DefaultProtocol()))
        
    def test_try_create_instance_with_BroadcastIPv4Address(self):
        self.assertRaises(TransportError, DatagramReceiver, BroadcastIPv4Address(5050), DefaultProtocol())
        
    def test_open_receiver(self):
        receiver = DatagramReceiver(BindIPv4Address(5050), DefaultProtocol())
        self.assertTrue(receiver.open())
        self.assertTrue(receiver.close())
        
    def test_bind_receiver(self):
        receiver = DatagramReceiver(BindIPv4Address(5051), DefaultProtocol())
        self.assertTrue(receiver.open())
        self.assertTrue(receiver.bind())
        self.assertTrue(receiver.close())
        
    def test_receive_stream(self):
        receiver = DatagramReceiver(BindIPv4Address(5051), DefaultProtocol())
        self.assertTrue(receiver.open())
        receiver._socket = pmock.Mock()
        receiver._socket.expects(pmock.once()).bind(pmock.eq(('', 5051)))
        self.assertTrue(receiver.bind())
        receiver._socket.expects(pmock.once()).close()
        receiver._socket.expects(pmock.once()).recvfrom(pmock.eq(1024)).will(pmock.return_value(("test", "")))
        self.assertEquals("test", receiver.receive())
        self.assertTrue(receiver.close())
    
    def test_try_bind_receiver_with_invalid_address(self):
        receiver = DatagramReceiver(IPv4Address("192.168", 5051), DefaultProtocol())
        self.assertTrue(receiver.open())
        self.assertRaises(BindError, receiver.bind)
        self.assertTrue(receiver.close())
    
    def test_reuse_address(self):
        receiver = DatagramReceiver(BindIPv4Address(5050), DefaultProtocol())
        self.assertTrue(receiver.open())
        self.assertTrue(receiver.reuseAddress(True))
        self.assertTrue(receiver.isReusingAddress())
        self.assertTrue(receiver.bind())
        self.assertTrue(receiver.close())
    
    def test_try_reuse_address_with_none_value_for_flag_parameter(self):
        receiver = DatagramReceiver(BindIPv4Address(5050), DefaultProtocol())
        self.assertTrue(receiver.open())
        self.assertRaises(RuntimeError, receiver.reuseAddress, None)
    
    def test_try_reuse_address_with_non_bool_value_for_flag_parameter(self):
        receiver = DatagramReceiver(BindIPv4Address(5050), DefaultProtocol())
        self.assertTrue(receiver.open())
        self.assertRaises(TypeError, receiver.reuseAddress, 1)
        
    def test_try_receive_with_none_value_for_buffer_size_parameter(self):
        receiver = DatagramReceiver(BindIPv4Address(5051), DefaultProtocol())
        self.assertTrue(receiver.open())
        receiver._socket = pmock.Mock()
        receiver._socket.expects(pmock.once()).bind(pmock.eq(('', 5051)))
        self.assertTrue(receiver.bind())
        self.assertRaises(RuntimeError, receiver.receive, None)
        self.assertTrue(receiver.close())
    
    def test_try_receive_with_invalid_value_for_buffer_size_parameter(self):
        receiver = DatagramReceiver(BindIPv4Address(5051), DefaultProtocol())
        self.assertTrue(receiver.open())
        receiver._socket = pmock.Mock()
        receiver._socket.expects(pmock.once()).bind(pmock.eq(('', 5051)))
        self.assertTrue(receiver.bind())
        self.assertRaises(RuntimeError, receiver.receive, 0)
        self.assertTrue(receiver.close())
    
    def test_try_receive_with_non_int_value_for_buffer_size_parameter(self):
        receiver = DatagramReceiver(BindIPv4Address(5051), DefaultProtocol())
        self.assertTrue(receiver.open())
        receiver._socket = pmock.Mock()
        receiver._socket.expects(pmock.once()).bind(pmock.eq(('', 5051)))
        self.assertTrue(receiver.bind())
        self.assertRaises(TypeError, receiver.receive, "1024")
        self.assertTrue(receiver.close())