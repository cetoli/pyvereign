from org.pyvereign.core.platform.DefaultCoreService import DefaultCoreService
from org.pyvereign.core.id.ID import ID
from org.pyvereign.core.context.Context import Context
from org.pyvereign.core.exception.ModuleError import ModuleError
import unittest

class DefaultCoreServiceTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertTrue(DefaultCoreService())
        service = DefaultCoreService()
        self.assertEquals(DefaultCoreService.NON_INITIALIZED, service.getStatus())
        
    def test_initialize_service(self):
        self.assertTrue(DefaultCoreService())
        service = DefaultCoreService()
        self.assertEquals(DefaultCoreService.NON_INITIALIZED, service.getStatus())
        service.initialize(service, DefaultCoreServiceTest.IDForTest(), DefaultCoreServiceTest.ContextForTest())
        self.assertEquals(DefaultCoreService.INITIALIZED, service.getStatus())
    
    def test_start_service(self):
        self.assertTrue(DefaultCoreService())
        service = DefaultCoreService()
        self.assertEquals(DefaultCoreService.NON_INITIALIZED, service.getStatus())
        service.initialize(service, DefaultCoreServiceTest.IDForTest(), DefaultCoreServiceTest.ContextForTest())
        self.assertEquals(DefaultCoreService.INITIALIZED, service.getStatus())
        service.start([])
        self.assertEquals(DefaultCoreService.STARTED, service.getStatus())
        
    def test_stop_service(self):
        self.assertTrue(DefaultCoreService())
        service = DefaultCoreService()
        self.assertEquals(DefaultCoreService.NON_INITIALIZED, service.getStatus())
        service.initialize(service, DefaultCoreServiceTest.IDForTest(), DefaultCoreServiceTest.ContextForTest())
        self.assertEquals(DefaultCoreService.INITIALIZED, service.getStatus())
        service.start([])
        self.assertEquals(DefaultCoreService.STARTED, service.getStatus())
        service.stop()
        self.assertEquals(DefaultCoreService.STOPED, service.getStatus())
        
    def test_try_start_service_without_inicialization(self):
        self.assertTrue(DefaultCoreService())
        service = DefaultCoreService()
        self.assertRaises(ModuleError, service.start, [])
        
    def test_try_start_two_times(self):
        self.assertTrue(DefaultCoreService())
        service = DefaultCoreService()
        self.assertEquals(DefaultCoreService.NON_INITIALIZED, service.getStatus())
        service.initialize(service, DefaultCoreServiceTest.IDForTest(), DefaultCoreServiceTest.ContextForTest())
        self.assertEquals(DefaultCoreService.INITIALIZED, service.getStatus())
        service.start([])
        self.assertEquals(DefaultCoreService.STARTED, service.getStatus())
        self.assertRaises(ModuleError, service.start, [])
    
    def test_try_initialize_service_with_service_already_running(self):
        self.assertTrue(DefaultCoreService())
        service = DefaultCoreService()
        self.assertEquals(DefaultCoreService.NON_INITIALIZED, service.getStatus())
        service.initialize(service, DefaultCoreServiceTest.IDForTest(), DefaultCoreServiceTest.ContextForTest())
        self.assertEquals(DefaultCoreService.INITIALIZED, service.getStatus())
        service.start([])
        self.assertEquals(DefaultCoreService.STARTED, service.getStatus())
        self.assertRaises(ModuleError, service.initialize, service, DefaultCoreServiceTest.IDForTest(), DefaultCoreServiceTest.ContextForTest())
    
    def test_getID(self):
        self.assertTrue(DefaultCoreService())
        service = DefaultCoreService()
        self.assertEquals(DefaultCoreService.NON_INITIALIZED, service.getStatus())
        id = DefaultCoreServiceTest.IDForTest()
        service.initialize(service, id, DefaultCoreServiceTest.ContextForTest())
        self.assertEquals(id, service.getID())
        
    def test_getContext(self):
        self.assertTrue(DefaultCoreService())
        service = DefaultCoreService()
        self.assertEquals(DefaultCoreService.NON_INITIALIZED, service.getStatus())
        context = DefaultCoreServiceTest.ContextForTest()
        service.initialize(service, DefaultCoreServiceTest.IDForTest(), context)
        self.assertEquals(DefaultCoreService.INITIALIZED, service.getStatus())
        self.assertEquals(context, service.getContext())
    
    def test_getInterface(self):
        service = DefaultCoreService()
        self.assertEquals(service, service.getInterface())
        
    def test_getOwner(self):
        self.assertTrue(DefaultCoreService())
        service = DefaultCoreService()
        self.assertEquals(DefaultCoreService.NON_INITIALIZED, service.getStatus())
        context = DefaultCoreServiceTest.ContextForTest()
        service.initialize(service, DefaultCoreServiceTest.IDForTest(), context)
        self.assertEquals(service, service.getOwner())
    
    def test_addModule(self):
        self.assertRaises(RuntimeError, DefaultCoreService().addModule, "123", DefaultCoreService())
        
    def test_removeModule(self):
        self.assertRaises(RuntimeError, DefaultCoreService().removeModule, "123")
        
    def test_countModules(self):
        self.assertEquals(0, DefaultCoreService().countModules())
        
    def test_clear_modules(self):
        self.assertRaises(RuntimeError, DefaultCoreService().clearModules)
    
    class IDForTest(ID):
        
        def __init__(self):
            return
        
    class ContextForTest(Context):
        
        def __init__(self):
            return