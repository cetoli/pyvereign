from atlas.api.env.transport.listener.StreamListener import StreamListener
from atlas.api.env.Environment import Environment
from atlas.api.env.transport.receiver.StreamReceiver import StreamReceiver
from atlas.api.env.transport.address.BindIPv4Address import BindIPv4Address
from atlas.api.env.networking.DefaultProtocol import DefaultProtocol
from atlas.api.env.transport.listener.TransportListener import TransportListener
from atlas.api.exception.TransportError import TransportError
import time
import unittest

environment = Environment()
environment.initialize()
environment.start()


class StreamListenerTest(unittest.TestCase):
    
    def test_open_close_stream_listener_with_stream_receiver(self):
        protocol = DefaultProtocol()
        protocol.setName("TCP")
        stream = StreamListener(environment, StreamReceiver(BindIPv4Address(5060), protocol))
        self.assertTrue(stream.open(5060))
        self.assertEquals(1024, stream.getBufferSize())
        self.assertTrue(stream.reuseAddress(True))
        stream.start()
        time.sleep(1)
        self.assertTrue(stream.close())
        
    def test_open_close_stream_listener_with_datagram_receiver(self):
        protocol = DefaultProtocol()
        protocol.setName("UDP")
        stream = StreamListener(environment, StreamReceiver(BindIPv4Address(5060), protocol))
        self.assertTrue(stream.open(5060))
        self.assertTrue(stream.reuseAddress(True))
        stream.start()
        self.assertTrue(stream.close())
        
    def test_add_transport_listener(self):
        protocol = DefaultProtocol()
        protocol.setName("TCP")
        streamListener = StreamListener(environment, StreamReceiver(BindIPv4Address(5060), protocol))
        transp = StreamListenerTest.TransportListenerForTest()
        self.assertEquals(transp, streamListener.addTransportListener("TCP://127.0.0.1:5050", transp))
        self.assertEquals(transp, streamListener.getTransportListener("TCP://127.0.0.1:5050"))
        self.assertEquals(1, streamListener.getNumberOfTransportListeners())
        
    def test_remove_transport_listener(self):
        protocol = DefaultProtocol()
        protocol.setName("TCP")
        streamListener = StreamListener(environment, StreamReceiver(BindIPv4Address(5060), protocol))
        transp = StreamListenerTest.TransportListenerForTest()
        self.assertEquals(transp, streamListener.addTransportListener("TCP://127.0.0.1:5050", transp))
        self.assertEquals(1, streamListener.getNumberOfTransportListeners())
        self.assertEquals(transp, streamListener.getTransportListener("TCP://127.0.0.1:5050"))
        self.assertEquals(transp, streamListener.removeTransportListener("TCP://127.0.0.1:5050"))
        self.assertEquals(0, streamListener.getNumberOfTransportListeners())
    
    def test_try_add_transport_listener_with_none_uri(self):
        stream = StreamListener(environment, StreamReceiver(BindIPv4Address(5060), DefaultProtocol()))
        self.assertRaises(RuntimeError, stream.addTransportListener, None, StreamListenerTest.TransportListenerForTest)
        
    def test_try_add_transport_listener_with_none_listener(self):
        stream = StreamListener(environment, StreamReceiver(BindIPv4Address(5060), DefaultProtocol()))
        self.assertRaises(RuntimeError, stream.addTransportListener, "TCP://127.0.0.1:5050", None)
        
    def test_try_get_transport_listener_with_invalid_uri(self):
        stream = StreamListener(environment, StreamReceiver(BindIPv4Address(5060), DefaultProtocol()))
        self.assertRaises(TypeError, stream.getTransportListener, 123)
        
    def test_try_get_transport_listener_none_uri(self):
        stream = StreamListener(environment, StreamReceiver(BindIPv4Address(5060), DefaultProtocol()))
        self.assertRaises(RuntimeError, stream.getTransportListener, None)
        
    def test_try_remove_transport_listener_with_invalid_uri(self):
        stream = StreamListener(environment, StreamReceiver(BindIPv4Address(5060), DefaultProtocol()))
        self.assertRaises(TypeError, stream.removeTransportListener, 123)
        
    def test_try_remove_transport_listener_none_uri(self):
        stream = StreamListener(environment, StreamReceiver(BindIPv4Address(5060), DefaultProtocol()))
        self.assertRaises(RuntimeError, stream.removeTransportListener, None)
        
    def test_get_number_of_transport_listeners(self):
        stream = StreamListener(environment, StreamReceiver(BindIPv4Address(5060), DefaultProtocol()))
        self.assertEquals(0, stream.getNumberOfTransportListeners())
        
    def test_set_buffer_size(self):
        stream = StreamListener(environment, StreamReceiver(BindIPv4Address(5060), DefaultProtocol()))
        self.assertEquals(2048, stream.setBufferSize(2048))
    
    def test_set_none_buffer_size(self):
        stream = StreamListener(environment, StreamReceiver(BindIPv4Address(5060), DefaultProtocol()))
        self.assertRaises(RuntimeError, stream.setBufferSize, None)
        
    def test_set_negative_buffer_size(self):
        stream = StreamListener(environment, StreamReceiver(BindIPv4Address(5060), DefaultProtocol()))
        self.assertRaises(RuntimeError, stream.setBufferSize, -1)
        
    def test_set_zero_buffer_size(self):
        stream = StreamListener(environment, StreamReceiver(BindIPv4Address(5060), DefaultProtocol()))
        self.assertRaises(RuntimeError, stream.setBufferSize, 0)
    
    def test_try_open_listerner_with_none_port(self):
        stream = StreamListener(environment, StreamReceiver(BindIPv4Address(5060), DefaultProtocol()))
        self.assertRaises(RuntimeError, stream.open, None)
        
    def test_try_open_listerner_with_negative_port(self):
        stream = StreamListener(environment, StreamReceiver(BindIPv4Address(5060), DefaultProtocol()))
        self.assertRaises(RuntimeError, stream.open, -1)
        
    def test_try_open_with_invalid_type_for_port(self):
        stream = StreamListener(environment, StreamReceiver(BindIPv4Address(5060), DefaultProtocol()))
        self.assertRaises(TypeError, stream.open, "5060")
        
    def test_try_setbuffersize_with_invalid_type_for_buffer(self):
        stream = StreamListener(environment, StreamReceiver(BindIPv4Address(5060), DefaultProtocol()))
        self.assertRaises(TypeError, stream.setBufferSize, "5060")
    
    def test_try_reuseaddress_with_invalid_type_for_flag(self):
        stream = StreamListener(environment, StreamReceiver(BindIPv4Address(5060), DefaultProtocol()))
        self.assertRaises(TypeError, stream.reuseAddress, "True")
        
    def test_try_reuse_address_with_true_flag(self):
        stream = StreamListener(environment, StreamReceiver(BindIPv4Address(5060), DefaultProtocol()))
        self.assertRaises(TransportError, stream.reuseAddress, True)
        
    def test_try_open_listerner_with_zero_port(self):
        stream = StreamListener(environment, StreamReceiver(BindIPv4Address(5060), DefaultProtocol()))
        self.assertRaises(RuntimeError, stream.open, 0)
    
    
    class TransportListenerForTest(TransportListener):
        
        def __init__(self):
            self._stream = None    
            
        def processStream(self, stream):
            self._stream = stream

        