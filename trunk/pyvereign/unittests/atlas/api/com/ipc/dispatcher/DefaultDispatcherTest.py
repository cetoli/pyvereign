from atlas.api.com.ipc.dispatcher.DefaultDispatcher import DefaultDispatcher
from atlas.api.com.ipc.handler.DefaultEventHandler import DefaultEventHandler
import unittest

class DefaultDispatcherTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(DefaultDispatcher())
        
    def test_register_event_handler(self):
        dispatcher = DefaultDispatcher()
        handler = DefaultEventHandler()
        self.assertEquals(handler, dispatcher.registerEventHandler(handler))
        self.assertEquals(1, dispatcher.getNumberOfEventHandlers())
        
    def test_unregister_event_handler(self):
        dispatcher = DefaultDispatcher()
        handler = DefaultEventHandler()
        self.assertEquals(handler, dispatcher.registerEventHandler(handler))
        self.assertEquals(1, dispatcher.getNumberOfEventHandlers())
        
        self.assertEquals(handler, dispatcher.unregisterEventHandler(handler.getHandle()))
        self.assertEquals(0, dispatcher.getNumberOfEventHandlers())
        
    