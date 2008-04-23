from org.pyvereign.core.communication.format.MessageFormatFactoryConfigurator import MessageFormatFactoryConfigurator
from org.pyvereign.util.Constants import Constants
from org.pyvereign.core.configuration.repository.ObjectRepositoryFactory import ObjectRepositoryFactory
from org.pyvereign.core.communication.format.MessageFormatFactory import MessageFormatFactory
from org.pyvereign.core.communication.format.JSONMessageFormat import JSONMessageFormat
import unittest

class MessageFormatFactoryConfiguratorTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(MessageFormatFactoryConfigurator())
        
    def test_load_configuration_create_object(self):
        configurator = MessageFormatFactoryConfigurator()
        self.assertEquals(Constants.MESSAGE_FORMATS_CONFIG_FILE, configurator.setFilename(Constants.MESSAGE_FORMATS_CONFIG_FILE))
        repository = ObjectRepositoryFactory().createObjectRepository(Constants.DEFAULT_OBJECT_REPOSITORY)
        self.assertEquals(repository, configurator.setObjectRepository(repository))
        
        configurator.loadConfiguration()
        configurator.createObjects()
        
        self.assertTrue(repository.getObject(Constants.JSON))
    
    def test_configure_object(self):
        configurator = MessageFormatFactoryConfigurator()
        self.assertEquals(Constants.MESSAGE_FORMATS_CONFIG_FILE, configurator.setFilename(Constants.MESSAGE_FORMATS_CONFIG_FILE))
        repository = ObjectRepositoryFactory().createObjectRepository(Constants.DEFAULT_OBJECT_REPOSITORY)
        self.assertEquals(repository, configurator.setObjectRepository(repository))
        
        configurator.loadConfiguration()
        configurator.createObjects()
        
        self.assertTrue(configurator.configureObject(MessageFormatFactory()))
        factory = configurator.configureObject(MessageFormatFactory())
        self.assertEquals(JSONMessageFormat, factory.createMessageFormat(Constants.JSON).__class__)