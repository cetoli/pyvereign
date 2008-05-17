from org.pyvereign.core.communication.endpoint.protocol.AbstractMessageReceiver import AbstractMessageReceiver
import unittest

class AbstractMessageReceiverTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, AbstractMessageReceiver)