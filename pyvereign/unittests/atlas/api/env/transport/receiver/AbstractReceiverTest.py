from atlas.api.env.transport.receiver.AbstractReceiver import AbstractReceiver
import unittest

class AbstractReceiverTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, AbstractReceiver)