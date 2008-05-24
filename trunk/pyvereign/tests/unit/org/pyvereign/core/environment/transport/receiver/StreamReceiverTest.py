from org.pyvereign.core.environment.transport.receiver.StreamReceiver import StreamReceiver
from org.pyvereign.core.environment.transport.address.IPv4Address import IPv4Address
from org.pyvereign.core.environment.transport.address.BindIPv4Address import BindIPv4Address
from org.pyvereign.core.exception.TransportError import TransportError
from org.pyvereign.core.environment.transport.address.BroadcastIPv4Address import BroadcastIPv4Address
from org.pyvereign.core.exception.BindError import BindError
from org.pyvereign.core.environment.instrumentation.dto.networking.NetworkProtocolImpl import NetworkProtocolImpl
import pmock
import unittest

class StreamReceiverTest(unittest.TestCase):
    
    def test_create_instance_with_IPv4Address(self):
        self.assertTrue(StreamReceiver(IPv4Address("192.168.1.2", 5050), NetworkProtocolImpl({})))
        
    def test_create_instance_with_BindIPv4Address(self):
        self.assertTrue(StreamReceiver(BindIPv4Address(5050), NetworkProtocolImpl({})))
        
    def test_try_create_instance_with_BroadcastIPv4Address(self):
        self.assertRaises(TransportError, StreamReceiver, BroadcastIPv4Address(5050), NetworkProtocolImpl({}))
    
    def test_open_receiver(self):
        receiver = StreamReceiver(BindIPv4Address(5050), NetworkProtocolImpl({}))
        self.assertTrue(receiver.open())
        self.assertTrue(receiver.close())
        
    def test_bind_receiver(self):
        receiver = StreamReceiver(BindIPv4Address(5053), NetworkProtocolImpl({}))
        self.assertTrue(receiver.open())
        self.assertTrue(receiver.bind())
        self.assertTrue(receiver.close())
        
    def test_receive_stream(self):
        receiver = StreamReceiver(BindIPv4Address(5051), NetworkProtocolImpl({}))
        self.assertTrue(receiver.open())
        receiver._socket = pmock.Mock()
        receiver._socket.expects(pmock.once()).bind(pmock.eq(('', 5051)))
        self.assertTrue(receiver.bind())
        receiver._socket.expects(pmock.once()).listen(pmock.eq(1))
        conn = pmock.Mock()
        conn.expects(pmock.once()).recv(pmock.eq(1024)).will(pmock.return_value("test"))
        receiver._socket.expects(pmock.once()).accept().will(pmock.return_value((conn, "")))
        self.assertEquals("test", receiver.receive())
        receiver._socket.expects(pmock.once()).close()
        self.assertTrue(receiver.close())
    
    def test_try_bind_receiver_with_invalid_address(self):
        receiver = StreamReceiver(IPv4Address("192.168", 5051), NetworkProtocolImpl({}))
        self.assertTrue(receiver.open())
        self.assertRaises(BindError, receiver.bind)
        self.assertTrue(receiver.close())
    
    def test_reuse_address(self):
        receiver = StreamReceiver(BindIPv4Address(5050), NetworkProtocolImpl({}))
        self.assertTrue(receiver.open())
        self.assertTrue(receiver.reuseAddress(True))
        self.assertTrue(receiver.isReusingAddress())
        self.assertTrue(receiver.bind())
        self.assertTrue(receiver.close())
    
    def test_try_reuse_address_with_none_value_for_flag_parameter(self):
        receiver = StreamReceiver(BindIPv4Address(5050), NetworkProtocolImpl({}))
        self.assertTrue(receiver.open())
        self.assertRaises(RuntimeError, receiver.reuseAddress, None)
    
    def test_try_reuse_address_with_non_bool_value_for_flag_parameter(self):
        receiver = StreamReceiver(BindIPv4Address(5050), NetworkProtocolImpl({}))
        self.assertTrue(receiver.open())
        self.assertRaises(TypeError, receiver.reuseAddress, 1)
        
    def test_try_receive_with_none_value_for_buffer_size_parameter(self):
        receiver = StreamReceiver(BindIPv4Address(5051), NetworkProtocolImpl({}))
        self.assertTrue(receiver.open())
        receiver._socket = pmock.Mock()
        receiver._socket.expects(pmock.once()).bind(pmock.eq(('', 5051)))
        self.assertTrue(receiver.bind())
        self.assertRaises(RuntimeError, receiver.receive, None)
        self.assertTrue(receiver.close())
    
    def test_try_receive_with_invalid_value_for_buffer_size_parameter(self):
        receiver = StreamReceiver(BindIPv4Address(5051), NetworkProtocolImpl({}))
        self.assertTrue(receiver.open())
        receiver._socket = pmock.Mock()
        receiver._socket.expects(pmock.once()).bind(pmock.eq(('', 5051)))
        self.assertTrue(receiver.bind())
        self.assertRaises(RuntimeError, receiver.receive, 0)
        self.assertTrue(receiver.close())
    
    def test_try_receive_with_non_int_value_for_buffer_size_parameter(self):
        receiver = StreamReceiver(BindIPv4Address(5051), NetworkProtocolImpl({}))
        self.assertTrue(receiver.open())
        receiver._socket = pmock.Mock()
        receiver._socket.expects(pmock.once()).bind(pmock.eq(('', 5051)))
        self.assertTrue(receiver.bind())
        self.assertRaises(TypeError, receiver.receive, "1024")
        self.assertTrue(receiver.close())
        
    def test_try_bind_with_non_opened_receiver(self):
        receiver = StreamReceiver(BindIPv4Address(5051), NetworkProtocolImpl({}))
        self.assertRaises(TransportError, receiver.bind)
        
    def test_try_receive_with_non_opened_receiver(self):
        receiver = StreamReceiver(BindIPv4Address(5051), NetworkProtocolImpl({}))
        self.assertRaises(TransportError, receiver.receive)