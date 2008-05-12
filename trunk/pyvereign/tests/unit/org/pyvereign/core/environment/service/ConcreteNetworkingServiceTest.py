from org.pyvereign.core.environment.service.DefaultNetworkingService import DefaultNetworkingService
from org.pyvereign.core.environment.service.ConcreteNetworkingService import ConcreteNetworkingService
from org.pyvereign.core.environment.Environment import Environment
from org.pyvereign.core.id.IDFactory import IDFactory
from org.pyvereign.core.context.Context import Context
from org.pyvereign.core.exception.ModuleError import ModuleError
from org.pyvereign.util.Constants import Constants
import unittest

class ConcreteNetworkingServiceTest(unittest.TestCase):
    
    def test_create_instance(self):
        default = DefaultNetworkingService()
        self.assertTrue(ConcreteNetworkingService(default))
        self.assertEquals(DefaultNetworkingService.NON_INITIALIZED, default.getStatus())
    
    def test_initialize_service(self):
        default = DefaultNetworkingService()
        service = ConcreteNetworkingService(default)
        self.assertEquals(DefaultNetworkingService.NON_INITIALIZED, service.getStatus())
        environment = Environment()
        id = IDFactory().createCoreServiceID(environment.getName(), service.getName())
        service.initialize(environment, id, ContextForTest())
        self.assertEquals(DefaultNetworkingService.INITIALIZED, service.getStatus())
    
    def test_start_service(self):
        default = DefaultNetworkingService()
        service = ConcreteNetworkingService(default)
        self.assertEquals(DefaultNetworkingService.NON_INITIALIZED, service.getStatus())
        environment = Environment()
        id = IDFactory().createCoreServiceID(environment.getName(), service.getName())
        service.initialize(environment, id, ContextForTest())
        self.assertEquals(DefaultNetworkingService.INITIALIZED, service.getStatus())
        service.start([])
        self.assertEquals(DefaultNetworkingService.STARTED, service.getStatus())
        
    def test_stop_service(self):
        default = DefaultNetworkingService()
        service = ConcreteNetworkingService(default)
        self.assertEquals(DefaultNetworkingService.NON_INITIALIZED, service.getStatus())
        environment = Environment()
        id = IDFactory().createCoreServiceID(environment.getName(), service.getName())
        service.initialize(environment, id, ContextForTest())
        self.assertEquals(DefaultNetworkingService.INITIALIZED, service.getStatus())
        service.start([])
        self.assertEquals(DefaultNetworkingService.STARTED, service.getStatus())
        service.stop()
        self.assertEquals(DefaultNetworkingService.STOPED, service.getStatus())
        
    def test_get_protocols(self):
        default = DefaultNetworkingService()
        service = ConcreteNetworkingService(default)
        self.assertEquals(DefaultNetworkingService.NON_INITIALIZED, service.getStatus())
        environment = Environment()
        id = IDFactory().createCoreServiceID(environment.getName(), service.getName())
        service.initialize(environment, id, ContextForTest())
        self.assertEquals(DefaultNetworkingService.INITIALIZED, service.getStatus())
        service.start([])
        self.assertEquals(DefaultNetworkingService.STARTED, service.getStatus())
        
        self.assertTrue(service.getNetworkProtocols())
        self.assertTrue(len(service.getNetworkProtocols()) > 0)
    
    def test_try_start_service_without_initialize_it(self):
        default = DefaultNetworkingService()
        service = ConcreteNetworkingService(default)
        self.assertRaises(ModuleError, service.start, [])
        
    def test_try_get_protocols_without_start_service(self):
        default = DefaultNetworkingService()
        service = ConcreteNetworkingService(default)
        self.assertRaises(ModuleError, service.getNetworkProtocols)

    def test_trye_add_module(self):
        default = DefaultNetworkingService()
        service = ConcreteNetworkingService(default)
        environment = Environment()
        id = IDFactory().createCoreServiceID(environment.getName(), service.getName())
    
        self.assertRaises(RuntimeError, service.addModule, id, service)
        
    def test_try_remove_module(self):
        default = DefaultNetworkingService()
        service = ConcreteNetworkingService(default)
        environment = Environment()
        id = IDFactory().createCoreServiceID(environment.getName(), service.getName())
        
        self.assertRaises(RuntimeError, service.removeModule, id)
        
    def test_try_clear_modules(self):
        self.assertRaises(RuntimeError, ConcreteNetworkingService(DefaultNetworkingService()).clearModules)
        
    def test_count_modules(self):
        default = DefaultNetworkingService()
        service = ConcreteNetworkingService(default)
        environment = Environment()
        id = IDFactory().createCoreServiceID(environment.getName(), service.getName())
    
        self.assertRaises(RuntimeError, service.addModule, id, service)
        self.assertEquals(0, service.countModules())
        
    def test_iscomposite(self):
        default = DefaultNetworkingService()
        service = ConcreteNetworkingService(default)
        self.assertFalse(service.isComposite())
        
    def test_get_name(self):
        default = DefaultNetworkingService()
        service = ConcreteNetworkingService(default)
        self.assertEquals(Constants.NETWORKING_SERVICE, service.getName())
        
class ContextForTest(Context):
    
    def __init__(self):
        return     