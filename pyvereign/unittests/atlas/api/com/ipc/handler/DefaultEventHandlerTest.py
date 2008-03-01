from atlas.api.com.ipc.handler.DefaultEventHandler import DefaultEventHandler
from atlas.api.com.ipc.event.DefaultEvent import DefaultEvent
import unittest

class DefaultEventHandlerTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(DefaultEventHandler())
        
    def test_clone_event_handler(self):
        handler = DefaultEventHandler()
        clone = handler.clone()
        self.assertNotEquals(handler, clone)
        
    def test_handle_event(self):
        handler = DefaultEventHandler()
        event = DefaultEvent("TEST", "TEST", "TEST")
        handler.handleEvent(event)
        self.assertEquals(event, handler.getEvent())