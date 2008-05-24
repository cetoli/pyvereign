from org.pyvereign.core.communication.endpoint.protocol.MessageSender import MessageSender
import unittest

class MessageSenderTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, MessageSender)