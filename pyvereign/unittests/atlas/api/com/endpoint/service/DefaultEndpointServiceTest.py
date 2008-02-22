from atlas.api.com.endpoint.service.DefaultEndpointService import DefaultEndpointService
from atlas.api.com.endpoint.listener.EndpointListener import EndpointListener
from atlas.api.microkernel.Microkernel import Microkernel
from atlas.api.com.Communication import Communication
import time
import unittest

Microkernel().initialize()
Microkernel().start()

class DefaultEndpointServiceTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(DefaultEndpointService())
        
    def test_add_endpoint_listener(self):
        service = DefaultEndpointService()
        service.initialize(Communication())
        listener = DefaultEndpointServiceTest.EndpointListenerForTest()
        self.assertEquals(listener, service.addEndpointListener("TCP://127.0.0.1:5050", listener))
        
    
    class EndpointListenerForTest(EndpointListener):
        
        def __init__(self):
            self._message = None
            
        def processMessage(self, message):
            self._message = message