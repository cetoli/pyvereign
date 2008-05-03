from org.pyvereign.util.Constants import Constants
from org.pyvereign.core.configuration.repository.ObjectRepositoryFactory import ObjectRepositoryFactory
from org.pyvereign.core.environment.instrumentation.dto.networking.NetworkingElementDTOFactory import NetworkingElementDTOFactory
from org.pyvereign.core.environment.instrumentation.dto.networking.NetworkingElementDTOFactoryConfigurator import NetworkingElementDTOFactoryConfigurator
from org.pyvereign.core.environment.instrumentation.dto.networking.NetworkProtocolImpl import NetworkProtocolImpl
from org.pyvereign.core.exception.NetworkingElementDTOFactoryError import NetworkingElementDTOFactoryError
import unittest

class NetworkingElementDTOFactoryTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(NetworkingElementDTOFactory())
        self.assertEquals(NetworkingElementDTOFactory(), NetworkingElementDTOFactory())
    
    def test_create_networking_elements(self):
        configurator = NetworkingElementDTOFactoryConfigurator()
        self.assertEquals(Constants.NETWORKING_ELEMENTS_CONFIG_FILE, configurator.setFilename(Constants.NETWORKING_ELEMENTS_CONFIG_FILE))
        repository = ObjectRepositoryFactory().createObjectRepository(Constants.DEFAULT_OBJECT_REPOSITORY)
        self.assertEquals(repository, configurator.setObjectRepository(repository))
        
        configurator.loadConfiguration()
        configurator.createObjects()
        
        self.assertTrue(configurator.configureObject(NetworkingElementDTOFactory()))
        
        factory = configurator.configureObject(NetworkingElementDTOFactory())
        
        self.assertTrue(factory.createNetworkingElement(Constants.NETWORK_PROTOCOL, {}))
        self.assertEquals(NetworkProtocolImpl, factory.createNetworkingElement(Constants.NETWORK_PROTOCOL, {}).__class__)
    
    def test_try_create_network_element_with_none_type(self):
        factory = NetworkingElementDTOFactory()
        
        self.assertRaises(TypeError, factory.createNetworkingElement, None, {})
        
    def test_try_create_network_element_with_invalid_type_for_name_parameter(self):
        factory = NetworkingElementDTOFactory()
        
        self.assertRaises(TypeError, factory.createNetworkingElement, 123, {})
        
    def test_try_create_network_element_with_unregistered_name_of_class(self):
        factory = NetworkingElementDTOFactory()
        
        self.assertRaises(NetworkingElementDTOFactoryError, factory.createNetworkingElement, "Teste", {})
        
    def test_registerNetworkingElementClass(self):
        factory = NetworkingElementDTOFactory()
        
        self.assertEquals(0, factory._clearNetworkingElementClasses())
        self.assertEquals(NetworkProtocolImpl, factory._registerNetworkingElementClass(Constants.NETWORK_PROTOCOL, NetworkProtocolImpl))
        self.assertEquals(1, factory._countNetworkingElementClasses())
        
    def test_try_register_network_element_class_none_name(self):
        factory = NetworkingElementDTOFactory()
        
        self.assertRaises(TypeError, factory._registerNetworkingElementClass, None, NetworkProtocolImpl)
        
    def test_try_register_network_element_class_none_class_object(self):
        factory = NetworkingElementDTOFactory()
        
        self.assertRaises(TypeError, factory._registerNetworkingElementClass, Constants.NETWORK_PROTOCOL, None)
        
    def test_try_register_network_element_class_with_invalid_type_for_name_parameter(self):
        factory = NetworkingElementDTOFactory()
        
        self.assertRaises(TypeError, factory._registerNetworkingElementClass, 123, NetworkProtocolImpl)
        
    def test_try_register_network_element_class_with_invalid_type_for_clazz_parameter(self):
        factory = NetworkingElementDTOFactory()
        
        self.assertRaises(TypeError, factory._registerNetworkingElementClass, Constants.NETWORK_PROTOCOL, 123)
    
    def test_unregisterNetworkingElementClass(self):
        factory = NetworkingElementDTOFactory()
        
        self.assertEquals(0, factory._clearNetworkingElementClasses())
        self.assertEquals(NetworkProtocolImpl, factory._registerNetworkingElementClass(Constants.NETWORK_PROTOCOL, NetworkProtocolImpl))
        self.assertEquals(1, factory._countNetworkingElementClasses())
        
        self.assertEquals(NetworkProtocolImpl, factory._unregisterNetworkingElementClass(Constants.NETWORK_PROTOCOL))
        self.assertEquals(0, factory._countNetworkingElementClasses())
    
    def test_try_unregister_network_element_class_with_none_name(self):
        factory = NetworkingElementDTOFactory()
        
        self.assertRaises(TypeError, factory._unregisterNetworkingElementClass, None)
        
    def test_try_unregister_network_element_class_with_invalid_type_for_name(self):
        factory = NetworkingElementDTOFactory()
        
        self.assertRaises(TypeError, factory._unregisterNetworkingElementClass, 123) 
        
    def test_try_create_network_element_with_none_values(self):
        factory = NetworkingElementDTOFactory()
        
        self.assertEquals(0, factory._clearNetworkingElementClasses())
        self.assertEquals(NetworkProtocolImpl, factory._registerNetworkingElementClass(Constants.NETWORK_PROTOCOL, NetworkProtocolImpl))
        
        self.assertRaises(TypeError, factory.createNetworkingElement, Constants.NETWORK_PROTOCOL, None)
        
    def test_try_create_network_element_with_invalid_type_for_values(self):
        factory = NetworkingElementDTOFactory()
        
        self.assertEquals(0, factory._clearNetworkingElementClasses())
        self.assertEquals(NetworkProtocolImpl, factory._registerNetworkingElementClass(Constants.NETWORK_PROTOCOL, NetworkProtocolImpl))
        
        self.assertRaises(TypeError, factory.createNetworkingElement, Constants.NETWORK_PROTOCOL, "123") 
        
    def test_try_unregister_non_existent_network_element_class(self):
        factory = NetworkingElementDTOFactory()
        
        self.assertRaises(NetworkingElementDTOFactoryError, factory._unregisterNetworkingElementClass, "TESTE")
    
    def test_clearNetworkingElementClasses(self):
        factory = NetworkingElementDTOFactory()
        
        self.assertEquals(0, factory._clearNetworkingElementClasses())
        self.assertEquals(NetworkProtocolImpl, factory._registerNetworkingElementClass(Constants.NETWORK_PROTOCOL, NetworkProtocolImpl))
        self.assertEquals(1, factory._countNetworkingElementClasses())
        
        self.assertEquals(0, factory._clearNetworkingElementClasses())
        self.assertEquals(0, factory._countNetworkingElementClasses())