from org.pyvereign.core.environment.transport.forwarder.Forwarder import Forwarder
import unittest

class ForwarderTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, Forwarder)