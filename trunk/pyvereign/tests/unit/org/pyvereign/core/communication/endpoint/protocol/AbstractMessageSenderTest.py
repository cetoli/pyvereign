from org.pyvereign.core.communication.endpoint.protocol.AbstractMessageSender import AbstractMessageSender
import unittest

class AbstractMessageSenderTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, AbstractMessageSender)