from org.pyvereign.core.environment.transport.forwarder.ForwarderFactory import ForwarderFactory
from org.pyvereign.core.environment.instrumentation.dto.networking.NetworkProtocolImpl import NetworkProtocolImpl
from org.pyvereign.core.environment.transport.forwarder.DatagramForwarder import DatagramForwarder
from org.pyvereign.core.environment.transport.address.IPv4Address import IPv4Address
from org.pyvereign.core.environment.transport.forwarder.StreamForwarder import StreamForwarder
import unittest

class ForwarderFactoryTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(ForwarderFactory())
        self.assertEquals(ForwarderFactory(), ForwarderFactory())
    
    def test_create_datagram_forwarder(self):
        protocol = NetworkProtocolImpl({"name": "UDP"})
        self.assertEquals(DatagramForwarder, ForwarderFactory().createForwarder(protocol.getName(), IPv4Address("192.168.0.15", 5050), protocol).__class__)
    
    def test_create_stream_forwarder(self):
        protocol = NetworkProtocolImpl({"name": "TCP"})
        self.assertEquals(StreamForwarder, ForwarderFactory().createForwarder(protocol.getName(), IPv4Address("192.168.0.15", 5050), protocol).__class__)