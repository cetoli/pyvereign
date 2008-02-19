from atlas.api.env.transport.listener.StreamListener import StreamListener
from atlas.api.env.Environment import Environment
from atlas.api.env.transport.receiver.StreamReceiver import StreamReceiver
from atlas.api.env.transport.address.BindIPv4Address import BindIPv4Address
from atlas.api.env.networking.DefaultProtocol import DefaultProtocol
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
        self.assertTrue(stream.open())
        stream.start()
        time.sleep(1)
        self.assertTrue(stream.close())

environment.stop()
        