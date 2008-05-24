from org.pyvereign.core.environment.transport.receiver.ReceiverFactory import ReceiverFactory
from org.pyvereign.core.environment.transport.address.IPv4Address import IPv4Address
from org.pyvereign.core.environment.transport.receiver.DatagramReceiver import DatagramReceiver
from org.pyvereign.core.environment.instrumentation.dto.networking.NetworkProtocolImpl import NetworkProtocolImpl
from org.pyvereign.core.environment.transport.receiver.StreamReceiver import StreamReceiver
import unittest

class ReceiverFactoryTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(ReceiverFactory())
        self.assertEquals(ReceiverFactory(), ReceiverFactory())
    
    def test_create_datagram_receiver(self):
        protocol = NetworkProtocolImpl({"name": "UDP"})
        self.assertEquals(DatagramReceiver, ReceiverFactory().createReceiver(protocol.getName(), IPv4Address("192.168.0.15", 5050), protocol).__class__)
    
    def test_create_stream_receiver(self):
        protocol = NetworkProtocolImpl({"name": "TCP"})
        self.assertEquals(StreamReceiver, ReceiverFactory().createReceiver(protocol.getName(), IPv4Address("192.168.0.15", 5050), protocol).__class__)