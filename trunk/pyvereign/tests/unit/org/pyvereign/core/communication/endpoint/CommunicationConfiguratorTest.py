from org.pyvereign.core.communication.CommunicationConfigurator import CommunicationConfigurator
from org.pyvereign.util.Constants import Constants
from org.pyvereign.core.configuration.repository.ObjectRepositoryFactory import ObjectRepositoryFactory
from org.pyvereign.core.communication.Communication import Communication
from org.pyvereign.core.id.IDFactory import IDFactory
import unittest

class CommunicationConfiguratorTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(CommunicationConfigurator())
        
    def test_load_configuration_create_objects(self):
        configurator = CommunicationConfigurator()
        self.assertEquals(Constants.COMMUNICATION_CONFIG_FILE, configurator.setFilename(Constants.COMMUNICATION_CONFIG_FILE))
        repository = ObjectRepositoryFactory().createObjectRepository(Constants.DEFAULT_OBJECT_REPOSITORY)
        self.assertEquals(repository, configurator.setObjectRepository(repository))
        
        configurator.loadConfiguration()
        configurator.createObjects()
        
        self.assertTrue(repository.getObject(Constants.ENDPOINT_SERVICE))
        
    
    def test_configure_object(self):
        configurator = CommunicationConfigurator()
        self.assertEquals(Constants.COMMUNICATION_CONFIG_FILE, configurator.setFilename(Constants.COMMUNICATION_CONFIG_FILE))
        repository = ObjectRepositoryFactory().createObjectRepository(Constants.DEFAULT_OBJECT_REPOSITORY)
        self.assertEquals(repository, configurator.setObjectRepository(repository))
        
        configurator.loadConfiguration()
        configurator.createObjects()
        
        self.assertTrue(repository.getObject(Constants.ENDPOINT_SERVICE))
        
        self.assertTrue(configurator.configureObject(Communication()))        
        communication = configurator.configureObject(Communication())
        
        self.assertTrue(communication.hasModule(IDFactory().createCoreServiceID(communication, Constants.ENDPOINT_SERVICE)))