from org.pyvereign.core.communication.endpoint.protocol.AbstractEndpointProtocol import AbstractEndpointProtocol
import unittest

class AbstractEndpointProtocolTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, AbstractEndpointProtocol)