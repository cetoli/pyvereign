from atlas.api.com.ipc.queue.EventQueue import EventQueue
import unittest

class EventQueueTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, EventQueue)