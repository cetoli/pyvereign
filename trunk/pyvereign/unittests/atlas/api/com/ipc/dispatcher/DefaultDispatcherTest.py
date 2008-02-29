from atlas.api.com.ipc.dispatcher.DefaultDispatcher import DefaultDispatcher
from atlas.api.com.ipc.handler.AbstractEventHandler import AbstractEventHandler
from atlas.api.com.ipc.event.Event import Event
from threading import Thread
import unittest

class DefaultDispatcherTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(DefaultDispatcher())
        
    def test_register_event_handler(self):
        handler = DefaultDispatcherTest.EventHandlerForTest()
        dispatcher = DefaultDispatcher()
        self.assertEquals(handler, dispatcher.registerEventHandler("test", handler))
        self.assertEquals(1, dispatcher.getNumberOfEventHandlers())
        
    def test_try_register_event_handler_with_none_handle(self):
        handler = DefaultDispatcherTest.EventHandlerForTest()
        dispatcher = DefaultDispatcher()
        self.assertRaises(RuntimeError, dispatcher.registerEventHandler, None, handler)
        
    def test_try_register_event_handler_with_none_handler(self):
        dispatcher = DefaultDispatcher()
        self.assertRaises(RuntimeError, dispatcher.registerEventHandler, "TEST", None)
        
    def test_unregister_event_handler(self):
        handler = DefaultDispatcherTest.EventHandlerForTest()
        dispatcher = DefaultDispatcher()
        self.assertEquals(handler, dispatcher.registerEventHandler("test", handler))
        self.assertEquals(1, dispatcher.getNumberOfEventHandlers())
        
        self.assertEquals(handler, dispatcher.unregisterEventHandler("test"))
        self.assertEquals(0, dispatcher.getNumberOfEventHandlers())
        
    def test_try_unregister_event_handler_with_none_handle(self):
        dispatcher = DefaultDispatcher()
        self.assertRaises(RuntimeError, dispatcher.unregisterEventHandler, None)
        
    def test_handle_envent(self):
        event = Event("TEST", "test", "test")
        handler = DefaultDispatcherTest.EventHandlerForTest()
        dispatcher = DefaultDispatcher()
        self.assertEquals(handler, dispatcher.registerEventHandler("TEST", handler))
        self.assertEquals(1, dispatcher.getNumberOfEventHandlers())
        self.assertTrue(dispatcher.handleEvent(event))
        handler = dispatcher.handleEvent(event)
        self.assertEquals(event, handler._event)
    
    
    class EventHandlerForTest(AbstractEventHandler):
        
        def __init__(self):
            Thread.__init__(self)
            self.initialize()