from atlas.api.com.ipc.queue.DefaultEventQueue import DefaultEventQueue
from atlas.api.com.ipc.event.DefaultEvent import DefaultEvent
from atlas.api.com.endpoint.message.EndpointMessage import EndpointMessage
from atlas.api.com.endpoint.address.EndpointAddress import EndpointAddress
import unittest

class DefaultEventQueueTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertTrue(DefaultEventQueue())
        
    def test_enqueue_event(self):
        queue = DefaultEventQueue()
        event = DefaultEvent("TEST", "test", "test")
        self.assertTrue(queue.enqueue(event))
        self.assertEquals(event, queue.enqueue(event))
        self.assertEquals(2, queue.getSize())
        
    def test_try_enqueue_none_event(self):
        queue = DefaultEventQueue()
        self.assertRaises(RuntimeError, queue.enqueue, None)
        
    def test_try_enqueue_invalid_type_for_event(self):
        queue = DefaultEventQueue()
        self.assertRaises(TypeError, queue.enqueue, "event")
        
    def test_dequeue_event(self):
        queue = DefaultEventQueue()
        event = DefaultEvent("TEST", "test", "test")
        self.assertTrue(queue.enqueue(event))
        self.assertEquals(event, queue.enqueue(event))
        self.assertEquals(2, queue.getSize())
        
        self.assertEquals(event, queue.dequeue())
    
    def test_process_message(self):
        origin = EndpointAddress.toEndpointAddress("TCP://127.0.0.1:5050")
        destination = EndpointAddress.toEndpointAddress("TCP://127.0.0.1:5050")
        event = DefaultEvent("TEST", "test", "test")
        message = EndpointMessage(origin, destination, event)
        queue = DefaultEventQueue()
        queue.processMessage(message)
        self.assertEquals(1, queue.getSize())
        self.assertEquals(event, queue.dequeue())