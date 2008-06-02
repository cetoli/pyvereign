from org.pyvereign.core.communication.ipc.event.Event import Event
import unittest

class EventTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, Event)