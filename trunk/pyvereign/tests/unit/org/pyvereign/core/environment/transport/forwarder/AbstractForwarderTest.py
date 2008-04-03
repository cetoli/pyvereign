from org.pyvereign.core.environment.transport.forwarder.AbstractForwarder import AbstractForwader
import unittest

class AbstractForwarderTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, AbstractForwader)