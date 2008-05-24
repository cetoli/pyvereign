from org.pyvereign.util.Constants import Constants
from org.pyvereign.core.configuration.repository.ObjectRepositoryFactory import ObjectRepositoryFactory
from org.pyvereign.core.environment.instrumentation.dto.system.SystemElementDTOFactory import SystemElementDTOFactory
from org.pyvereign.core.environment.instrumentation.dto.system.SystemElementDTOFactoryConfigurator import SystemElementDTOFactoryConfigurator
from org.pyvereign.core.environment.instrumentation.dto.system.ProcessImpl import ProcessImpl
from org.pyvereign.core.exception.SystemElementDTOFactoryError import SystemElementDTOFactoryError
import unittest

class SystemElementDTOFactoryTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(SystemElementDTOFactory())
        self.assertEquals(SystemElementDTOFactory(), SystemElementDTOFactory())
    
    def test_create_system_element(self):
        configurator = SystemElementDTOFactoryConfigurator()
        configurator.setFilename(Constants.SYSTEM_ELEMENTS_CONFIG_FILE)
        configurator.setObjectRepository(ObjectRepositoryFactory().createObjectRepository(Constants.DEFAULT_OBJECT_REPOSITORY))
        configurator.loadConfiguration()
        configurator.createObjects()
        
        factory = configurator.configureObject(SystemElementDTOFactory())
        
        self.assertEquals(ProcessImpl, factory.createSystemElement(Constants.PROCESS, {}).__class__)
    
    def test_try_create_system_element_with_none_type(self):
        factory = SystemElementDTOFactory()
        
        self.assertRaises(TypeError, factory.createSystemElement, None, {})
        
    def test_try_create_system_element_with_invalid_type_for_name_parameter(self):
        factory = SystemElementDTOFactory()
        
        self.assertRaises(TypeError, factory.createSystemElement, 123, {})
        
    def test_try_create_system_element_with_unregistered_name_of_class(self):
        factory = SystemElementDTOFactory()
        
        self.assertRaises(SystemElementDTOFactoryError, factory.createSystemElement, "Teste", {})
        
    def test_registerSystemElementClass(self):
        factory = SystemElementDTOFactory()
        
        self.assertEquals(0, factory._clearSystemElementClasses())
        self.assertEquals(ProcessImpl, factory._registerSystemElementClass(Constants.PROCESS, ProcessImpl))
        self.assertEquals(1, factory._countSystemElementClasses())
        
    def test_try_register_system_element_class_none_name(self):
        factory = SystemElementDTOFactory()
        
        self.assertRaises(TypeError, factory._registerSystemElementClass, None, ProcessImpl)
        
    def test_try_register_system_element_class_none_class_object(self):
        factory = SystemElementDTOFactory()
        
        self.assertRaises(TypeError, factory._registerSystemElementClass, Constants.PROCESS, None)
        
    def test_try_register_system_element_class_with_invalid_type_for_name_parameter(self):
        factory = SystemElementDTOFactory()
        
        self.assertRaises(TypeError, factory._registerSystemElementClass, 123, ProcessImpl)
        
    def test_try_register_system_element_class_with_invalid_type_for_clazz_parameter(self):
        factory = SystemElementDTOFactory()
        
        self.assertRaises(TypeError, factory._registerSystemElementClass, Constants.PROCESS, 123)
    
    def test_unregisterSystemElementClass(self):
        factory = SystemElementDTOFactory()
        
        self.assertEquals(0, factory._clearSystemElementClasses())
        self.assertEquals(ProcessImpl, factory._registerSystemElementClass(Constants.PROCESS, ProcessImpl))
        self.assertEquals(1, factory._countSystemElementClasses())
        
        self.assertEquals(ProcessImpl, factory._unregisterSystemElementClass(Constants.PROCESS))
        self.assertEquals(0, factory._countSystemElementClasses())
    
    def test_try_unregister_system_element_class_with_none_name(self):
        factory = SystemElementDTOFactory()
        
        self.assertRaises(TypeError, factory._unregisterSystemElementClass, None)
        
    def test_try_unregister_system_element_class_with_invalid_type_for_name(self):
        factory = SystemElementDTOFactory()
        
        self.assertRaises(TypeError, factory._unregisterSystemElementClass, 123) 
        
    def test_try_create_system_element_with_none_values(self):
        factory = SystemElementDTOFactory()
        
        self.assertEquals(0, factory._clearSystemElementClasses())
        self.assertEquals(ProcessImpl, factory._registerSystemElementClass(Constants.NETWORK_PROTOCOL, ProcessImpl))
        
        self.assertRaises(TypeError, factory.createSystemElement, Constants.PROCESS, None)
        
    def test_try_create_system_element_with_invalid_type_for_values(self):
        factory = SystemElementDTOFactory()
        
        self.assertEquals(0, factory._clearSystemElementClasses())
        self.assertEquals(ProcessImpl, factory._registerSystemElementClass(Constants.PROCESS, ProcessImpl))
        
        self.assertRaises(TypeError, factory.createSystemElement, Constants.PROCESS, "123") 
        
    def test_try_unregister_non_existent_system_element_class(self):
        factory = SystemElementDTOFactory()
        
        self.assertRaises(SystemElementDTOFactoryError, factory._unregisterSystemElementClass, "TESTE")
    
    def test_clearSystemElementClasses(self):
        factory = SystemElementDTOFactory()
        
        self.assertEquals(0, factory._clearSystemElementClasses())
        self.assertEquals(ProcessImpl, factory._registerSystemElementClass(Constants.PROCESS, ProcessImpl))
        self.assertEquals(1, factory._countSystemElementClasses())
        
        self.assertEquals(0, factory._clearSystemElementClasses())
        self.assertEquals(0, factory._countSystemElementClasses())