from org.pyvereign.core.communication.endpoint.protocol.EndpointProtocol import EndpointProtocol
import unittest

class EndpointProtocolTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, EndpointProtocol)