from org.pyvereign.core.environment.transport.receiver.Receiver import Receiver
import unittest

class ReceiverTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, Receiver)