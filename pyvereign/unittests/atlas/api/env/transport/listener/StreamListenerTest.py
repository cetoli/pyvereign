from atlas.api.env.transport.listener.StreamListener import StreamListener
from atlas.api.env.Environment import Environment
from atlas.api.env.transport.receiver.StreamReceiver import StreamReceiver
from atlas.api.env.transport.address.BindIPv4Address import BindIPv4Address
from atlas.api.env.networking.DefaultProtocol import DefaultProtocol
from atlas.api.env.transport.listener.TransportListener import TransportListener
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
        self.assertEquals(1, streamListener.getNumberOfTransportListeners())
        
    def test_remove_transport_listener(self):
        protocol = DefaultProtocol()
        protocol.setName("TCP")
        streamListener = StreamListener(environment, StreamReceiver(BindIPv4Address(5060), protocol))
        transp = StreamListenerTest.TransportListenerForTest()
        self.assertEquals(transp, streamListener.addTransportListener("TCP://127.0.0.1:5050", transp))
        self.assertEquals(1, streamListener.getNumberOfTransportListeners())
        
        self.assertEquals(transp, streamListener.removeTransportListener("TCP://127.0.0.1:5050"))
        self.assertEquals(0, streamListener.getNumberOfTransportListeners())
    
    class TransportListenerForTest(TransportListener):
        
        def __init__(self):
            self._stream = None    
            
        def processStream(self, stream):
            self._stream = stream

        