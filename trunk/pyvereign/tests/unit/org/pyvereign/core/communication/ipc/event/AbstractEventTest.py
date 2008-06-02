from org.pyvereign.core.communication.ipc.event.AbstractEvent import AbstractEvent
import unittest

class AbstractEventTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, AbstractEvent)