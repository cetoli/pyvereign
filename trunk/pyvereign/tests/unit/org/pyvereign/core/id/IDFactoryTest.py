from org.pyvereign.core.id.IDFactory import IDFactory
from org.pyvereign.core.id.CoreServiceID import CoreServiceID
from org.pyvereign.core.environment.Environment import Environment
from org.pyvereign.core.environment.service.DefaultTransportService import DefaultTransportService
from org.pyvereign.core.environment.service.DefaultNetworkingService import DefaultNetworkingService
from org.pyvereign.core.id.InternalServerID import InternalServerID
import unittest

class IDFactoryTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(IDFactory())
        self.assertEquals(IDFactory(), IDFactory())
        
    def test_create_core_service_with_environment_networking_service(self):
        self.assertTrue(Environment())
        environment = Environment()
        self.assertTrue(DefaultNetworkingService())
        service = DefaultTransportService()
        self.assertTrue(IDFactory().createCoreServiceID(environment, service.getName()))
        self.assertEquals(CoreServiceID, IDFactory().createCoreServiceID(environment, service.getName()).__class__)
    
    def test_create_core_service_with_environment_transport_service(self):
        self.assertTrue(Environment())
        environment = Environment()
        self.assertTrue(DefaultTransportService())
        service = DefaultTransportService()
        self.assertTrue(IDFactory().createCoreServiceID(environment, service.getName()))
        self.assertEquals(CoreServiceID, IDFactory().createCoreServiceID(environment, service.getName()).__class__)
    
    def test_create_internal_server_with_environment(self):
        self.assertTrue(Environment())
        environment = Environment()
        self.assertTrue(IDFactory().createInternalServerID(environment.getName()))
        self.assertEquals(InternalServerID, IDFactory().createInternalServerID(environment.getName()).__class__)
        
    