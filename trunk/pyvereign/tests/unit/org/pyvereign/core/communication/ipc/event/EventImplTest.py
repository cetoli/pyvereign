from org.pyvereign.core.communication.ipc.event.EventImpl import EventImpl
import unittest

class EventImplTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(EventImpl("TEST", "asd", "123"))