from atlas.api.com.ipc.queue.AbstractEventQueue import AbstractEventQueue
import unittest

class AbstractEventQueueTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, AbstractEventQueue)