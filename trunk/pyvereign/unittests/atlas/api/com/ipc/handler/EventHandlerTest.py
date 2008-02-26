from atlas.api.com.ipc.handler.EventHandler import EventHandler
import unittest

class EventHandlerTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, EventHandler)