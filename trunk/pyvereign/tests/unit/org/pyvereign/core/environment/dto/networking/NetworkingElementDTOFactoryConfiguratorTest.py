from org.pyvereign.core.environment.dto.networking.NetworkingElementDTOFactoryConfigurator import NetworkingElementDTOFactoryConfigurator
from org.pyvereign.util.Constants import Constants
from org.pyvereign.core.configuration.repository.ObjectRepositoryFactory import ObjectRepositoryFactory
from org.pyvereign.core.environment.dto.networking.NetworkProtocolImpl import NetworkProtocolImpl
from org.pyvereign.core.environment.dto.networking.NetworkingElementDTOFactory import NetworkingElementDTOFactory
import unittest

class NetworkingElementDTOFactoryConfiguratorTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(NetworkingElementDTOFactoryConfigurator())
    
    def test_load_configuration_create_objects(self):
        configurator = NetworkingElementDTOFactoryConfigurator()
        self.assertEquals(Constants.NETWORKING_ELEMENTS_CONFIG_FILE, configurator.setFilename(Constants.NETWORKING_ELEMENTS_CONFIG_FILE))
        repository = ObjectRepositoryFactory().createObjectRepository(Constants.DEFAULT_OBJECT_REPOSITORY)
        self.assertEquals(repository, configurator.setObjectRepository(repository))
        
        configurator.loadConfiguration()
        configurator.createObjects()
        
        self.assertTrue(repository.getObject(Constants.NETWORK_PROTOCOL))
        self.assertEquals(NetworkProtocolImpl, repository.getObject(Constants.NETWORK_PROTOCOL))

    def test_configure_object(self):
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