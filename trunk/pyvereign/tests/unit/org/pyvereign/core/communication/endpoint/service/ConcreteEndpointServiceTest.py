from org.pyvereign.core.communication.endpoint.service.DefaultEndpointService import DefaultEndpointService
from org.pyvereign.core.communication.endpoint.service.ConcreteEndpointService import ConcreteEndpointService
from org.pyvereign.core.microkernel.Microkernel import Microkernel
from org.pyvereign.core.id.IDFactory import IDFactory
from org.pyvereign.util.Constants import Constants
from org.pyvereign.core.microkernel.CoreServiceContext import CoreServiceContext
from org.pyvereign.core.communication.endpoint.listener.EndpointListener import EndpointListener
import unittest

class ConcreteEndpointServiceTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(ConcreteEndpointService(DefaultEndpointService()))
        service = ConcreteEndpointService(DefaultEndpointService())
        self.assertEquals(DefaultEndpointService.NON_INITIALIZED, service.getStatus())
        
    def test_initialize_service(self):
        service = ConcreteEndpointService(DefaultEndpointService())
        self.assertEquals(DefaultEndpointService.NON_INITIALIZED, service.getStatus())
        kernel = Microkernel()
        kernel.initialize()
        
        self.assertTrue(kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION)))
        communication = kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION))
        
        service.initialize(communication, IDFactory().createCoreServiceID(communication, Constants.ENDPOINT_SERVICE), CoreServiceContext(service))
        
        self.assertEquals(DefaultEndpointService.INITIALIZED, service.getStatus())
    
    def test_start_service(self):
        service = ConcreteEndpointService(DefaultEndpointService())
        self.assertEquals(DefaultEndpointService.NON_INITIALIZED, service.getStatus())
        kernel = Microkernel()
        self.assertEquals(Microkernel.NON_INITIALIZED, kernel.getStatus())
        kernel.initialize()
        self.assertEquals(Microkernel.INITIALIZED, kernel.getStatus())
        self.assertTrue(kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION)))
        communication = kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION))
        
        service.initialize(communication, IDFactory().createCoreServiceID(communication, Constants.ENDPOINT_SERVICE), CoreServiceContext(service))
        self.assertEquals(DefaultEndpointService.INITIALIZED, service.getStatus())
        service.start([])
        self.assertEquals(DefaultEndpointService.STARTED, service.getStatus())
        
    def test_stop_service(self):
        service = ConcreteEndpointService(DefaultEndpointService())
        self.assertEquals(DefaultEndpointService.NON_INITIALIZED, service.getStatus())
        kernel = Microkernel()
        kernel.initialize()
        
        self.assertTrue(kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION)))
        communication = kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION))
        
        service.initialize(communication, IDFactory().createCoreServiceID(communication, Constants.ENDPOINT_SERVICE), CoreServiceContext(service))
        self.assertEquals(DefaultEndpointService.INITIALIZED, service.getStatus())
        service.start([])
        self.assertEquals(DefaultEndpointService.STARTED, service.getStatus())
        service.stop()
        self.assertEquals(DefaultEndpointService.STOPED, service.getStatus())
        
    def test_add_endpoint_listener(self):
        service = ConcreteEndpointService(DefaultEndpointService())
        self.assertEquals(DefaultEndpointService.NON_INITIALIZED, service.getStatus())
        kernel = Microkernel()
        self.assertEquals(Microkernel.NON_INITIALIZED, kernel.getStatus())
        kernel.initialize()
        self.assertTrue(kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION)))
        communication = kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION))
        service.initialize(communication, IDFactory().createCoreServiceID(communication, Constants.ENDPOINT_SERVICE), CoreServiceContext(service))
        self.assertEquals(DefaultEndpointService.INITIALIZED, service.getStatus())
        
        listener = EndpointListenerForTest()

        self.assertEquals(listener, service.addEndpointListener("TCP://127.0.0.1:5050", listener))
        self.assertTrue(service.hasEndpointListener("TCP://127.0.0.1:5050"))
        self.assertEquals(listener, service.getEndpointListener("TCP://127.0.0.1:5050"))
    
    def test_try_add_endpoint_listener_with_none_uri(self):
        self.assertRaises(TypeError, ConcreteEndpointService(DefaultEndpointService()).addEndpointListener, None, EndpointListenerForTest())
        
    def test_try_add_endpoint_listener_with_none_listener(self):
        self.assertRaises(TypeError, ConcreteEndpointService(DefaultEndpointService()).addEndpointListener, "TCP://127.0.0.1:5050", None)
        
    def test_try_add_endpoint_listener_with_invalid_type_uri(self):
        self.assertRaises(TypeError, ConcreteEndpointService(DefaultEndpointService()).addEndpointListener, 123, EndpointListenerForTest())
    
    def test_try_add_endpoint_listener_with_invalid_type_listener(self):
        self.assertRaises(TypeError, ConcreteEndpointService(DefaultEndpointService()).addEndpointListener, "TCP://127.0.0.1:5050", "listener")
        
    def test_remove_endpoint_listener(self):
        service = ConcreteEndpointService(DefaultEndpointService())
        self.assertEquals(DefaultEndpointService.NON_INITIALIZED, service.getStatus())
        kernel = Microkernel()
        self.assertEquals(Microkernel.NON_INITIALIZED, kernel.getStatus())
        kernel.initialize()
        self.assertTrue(kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION)))
        communication = kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION))
        service.initialize(communication, IDFactory().createCoreServiceID(communication, Constants.ENDPOINT_SERVICE), CoreServiceContext(service))
        self.assertEquals(DefaultEndpointService.INITIALIZED, service.getStatus())
        
        listener = EndpointListenerForTest()
        
        self.assertEquals(listener, service.addEndpointListener("TCP://127.0.0.1:5050", listener))
        self.assertTrue(service.hasEndpointListener("TCP://127.0.0.1:5050"))
        self.assertEquals(listener, service.getEndpointListener("TCP://127.0.0.1:5050"))
        
        self.assertEquals(listener, service.removeEndpointListener("TCP://127.0.0.1:5050"))
        self.assertFalse(service.hasEndpointListener("TCP://127.0.0.1:5050"))
    
    def test_try_remove_endpoint_listener_with_none_uri(self):
        self.assertRaises(TypeError, ConcreteEndpointService(DefaultEndpointService()).removeEndpointListener, 1233)
        
    def test_try_remove_endpoint_listener_with_invalid_type_for_uri(self):
        self.assertRaises(TypeError, ConcreteEndpointService(DefaultEndpointService()).removeEndpointListener, None) 
    
        
        
class EndpointListenerForTest(EndpointListener):
    
    def __init__(self):
        self._e = 1