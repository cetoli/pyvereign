from org.pyvereign.core.communication.endpoint.protocol.EndpointProtocolCreator import EndpointProtocolCreator
from org.pyvereign.core.environment.instrumentation.dto.networking.NetworkProtocolImpl import NetworkProtocolImpl
from org.pyvereign.util.Constants import Constants
import unittest

class EndpointProtocolCreatorTest(unittest.TestCase):
    
    def test_create_endpoint_protocol(self):
        self.assertTrue(EndpointProtocolCreator.createEndpointProtocol(NetworkProtocolImpl({"name": "TCP"})))
        self.assertEquals(Constants.ENDPOINT_PROTOCOL_CLASS, EndpointProtocolCreator.createEndpointProtocol(NetworkProtocolImpl({"name": "TCP"})).__class__.__name__)