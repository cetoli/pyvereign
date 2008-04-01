from org.pyvereign.core.environment.dto.networking.NetworkingElementDTOFactory import NetworkingElementDTOFactory
from org.pyvereign.core.environment.dto.networking.NetworkingElementDTOFactoryConfigurator import NetworkingElementDTOFactoryConfigurator
from org.pyvereign.util.Constants import Constants
from org.pyvereign.core.configuration.repository.ObjectRepositoryFactory import ObjectRepositoryFactory
from org.pyvereign.core.environment.dto.networking.NetworkProtocolImpl import NetworkProtocolImpl
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
        