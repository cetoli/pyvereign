from org.pyvereign.core.communication.endpoint.protocol.MessageReceiver import MessageReceiver
import unittest

class MessageReceiverTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, MessageReceiver)