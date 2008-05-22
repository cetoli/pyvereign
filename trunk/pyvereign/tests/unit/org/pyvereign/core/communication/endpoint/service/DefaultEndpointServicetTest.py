from org.pyvereign.core.communication.endpoint.service.DefaultEndpointService import DefaultEndpointService
from org.pyvereign.core.microkernel.Microkernel import Microkernel
from org.pyvereign.core.id.IDFactory import IDFactory
from org.pyvereign.util.Constants import Constants
from org.pyvereign.core.microkernel.CoreServiceContext import CoreServiceContext
import unittest

class DefaultEndpointTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(DefaultEndpointService())
        service = DefaultEndpointService()
        self.assertEquals(DefaultEndpointService.NON_INITIALIZED, service.getStatus())
        
    def test_initialize_service(self):
        service = DefaultEndpointService()
        self.assertEquals(DefaultEndpointService.NON_INITIALIZED, service.getStatus())
        kernel = Microkernel()
        kernel.initialize()
        
        self.assertTrue(kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION)))
        communication = kernel.getModule(IDFactory().createInternalServerID(Constants.COMMUNICATION))
        
        service.initialize(communication, IDFactory().createCoreServiceID(communication, Constants.ENDPOINT_SERVICE), CoreServiceContext(service))
        
        self.assertEquals(DefaultEndpointService.INITIALIZED, service.getStatus())
        
    