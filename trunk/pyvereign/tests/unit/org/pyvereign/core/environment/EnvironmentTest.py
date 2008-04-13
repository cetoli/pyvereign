from org.pyvereign.core.environment.Environment import Environment
from org.pyvereign.core.microkernel.Microkernel import Microkernel
from org.pyvereign.core.id.IDFactory import IDFactory
from org.pyvereign.util.Constants import Constants
from org.pyvereign.core.context.Context import Context
from org.pyvereign.core.platform.Module import Module
from org.pyvereign.core.environment.service.DefaultNetworkingService import DefaultNetworkingService
from org.pyvereign.core.environment.service.DefaultTransportService import DefaultTransportService
from org.pyvereign.core.environment.EnvironmentConfigurator import EnvironmentConfigurator
import unittest

class EnvironmentTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(Environment())
        self.assertEquals(EnvironmentConfigurator, Environment()._getConfigurator().__class__)
        self.assertEquals(Constants.ENVIRONMENT_CONFIG_FILE, Environment()._getConfigurationFilename())
        self.assertEquals(Constants.DEFAULT_OBJECT_REPOSITORY_CLASS, Environment()._getObjectRepository().__class__)
    
    def test_initialize_environment(self):
        environment = Environment()
        self.assertEquals(Environment.NON_INITIALIZED, environment.getStatus())
        microkernel = Microkernel()
        id = IDFactory().createInternalServerID(Constants.ENVIRONMENT);
        environment.initialize(microkernel, id, ContextForTest())
        self.assertEquals(Environment.INITIALIZED, environment.getStatus())
        self.assertEquals(microkernel, environment.getOwner())
        self.assertEquals(id, environment.getID())
        self.assertTrue(environment.getModules())
        
        modules = environment.getModules()
        for m in modules:
            self.assertEquals(Module.INITIALIZED, m.getStatus())
            
    def test_start_environment(self):
        environment = Environment()
        self.assertEquals(Environment.NON_INITIALIZED, environment.getStatus())
        microkernel = Microkernel()
        id = IDFactory().createInternalServerID(Constants.ENVIRONMENT);
        environment.initialize(microkernel, id, ContextForTest())
        self.assertEquals(Environment.INITIALIZED, environment.getStatus())
        self.assertEquals(microkernel, environment.getOwner())
        self.assertEquals(id, environment.getID())
        self.assertTrue(environment.getModules())
        
        modules = environment.getModules()
        for m in modules:
            self.assertEquals(Module.INITIALIZED, m.getStatus())
        
        environment.start([])
        modules = environment.getModules()
        for m in modules:
            self.assertEquals(Module.STARTED, m.getStatus())
    
    def test_add_module(self):
        environment = Environment()
        networking = DefaultNetworkingService()
        transport = DefaultTransportService()
        idNetworking = IDFactory().createCoreServiceID(environment, networking.getName())
        idTransport = IDFactory().createCoreServiceID(environment, transport.getName())
        
        self.assertEquals(networking, environment.addModule(idNetworking, networking))
        self.assertEquals(1, environment.countModules())
        self.assertEquals(transport, environment.addModule(idTransport, transport))
        self.assertEquals(2, environment.countModules())
        
        self.assertEquals(networking, environment.getModule(idNetworking))
        self.assertEquals(transport, environment.getModule(idTransport))
        
    def test_try_add_module_with_none_id(self):
        environment = Environment()
        networking = DefaultNetworkingService()
        transport = DefaultTransportService()
        
        self.assertRaises(TypeError, environment.addModule, None, networking)
        self.assertEquals(0, environment.countModules())
        self.assertRaises(TypeError, environment.addModule, None, transport)
        self.assertEquals(0, environment.countModules())
        
    def test_try_add_module_with_none_service(self):
        environment = Environment()
        networking = DefaultNetworkingService()
        transport = DefaultTransportService()
        idNetworking = IDFactory().createCoreServiceID(environment, networking.getName())
        idTransport = IDFactory().createCoreServiceID(environment, transport.getName())
        
        self.assertRaises(TypeError, environment.addModule, idNetworking, None)
        self.assertEquals(0, environment.countModules())
        self.assertRaises(TypeError, environment.addModule, idTransport, None)
        self.assertEquals(0, environment.countModules())
    
    def test_remove_module(self):
        environment = Environment()
        networking = DefaultNetworkingService()
        transport = DefaultTransportService()
        idNetworking = IDFactory().createCoreServiceID(environment, networking.getName())
        idTransport = IDFactory().createCoreServiceID(environment, transport.getName())
        
        self.assertEquals(networking, environment.addModule(idNetworking, networking))
        self.assertEquals(1, environment.countModules())
        self.assertEquals(transport, environment.addModule(idTransport, transport))
        self.assertEquals(2, environment.countModules())
        
        self.assertEquals(networking, environment.getModule(idNetworking))
        self.assertEquals(transport, environment.getModule(idTransport))
        
        self.assertEquals(networking, environment.removeModule(idNetworking))
        self.assertEquals(1, environment.countModules())
        self.assertEquals(transport, environment.removeModule(idTransport))
        self.assertEquals(0, environment.countModules())
    
    def test_try_remove_module_with_none_id(self):
        self.assertRaises(TypeError, Environment().removeModule, None)
        
    def test_try_get_module_with_none_id(self):
        self.assertRaises(TypeError, Environment().getModule, None)
        
class ContextForTest(Context):
    
    def __init__(self):
        return