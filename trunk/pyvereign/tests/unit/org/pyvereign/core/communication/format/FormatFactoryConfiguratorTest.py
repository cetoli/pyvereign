from org.pyvereign.util.Constants import Constants
from org.pyvereign.core.configuration.repository.ObjectRepositoryFactory import ObjectRepositoryFactory
from org.pyvereign.core.communication.format.FormatFactoryConfigurator import FormatFactoryConfigurator
from org.pyvereign.core.communication.format.FormatFactory import FormatFactory
from org.pyvereign.core.communication.format.JSONFormat import JSONFormat
import unittest

class MessageFormatFactoryConfiguratorTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(FormatFactoryConfigurator())
        
    def test_load_configuration_create_object(self):
        configurator = FormatFactoryConfigurator()
        self.assertEquals(Constants.MESSAGE_FORMATS_CONFIG_FILE, configurator.setFilename(Constants.MESSAGE_FORMATS_CONFIG_FILE))
        repository = ObjectRepositoryFactory().createObjectRepository(Constants.DEFAULT_OBJECT_REPOSITORY)
        self.assertEquals(repository, configurator.setObjectRepository(repository))
        
        configurator.loadConfiguration()
        configurator.createObjects()
        
        self.assertTrue(repository.getObject(Constants.JSON))
    
    def test_configure_object(self):
        configurator = FormatFactoryConfigurator()
        self.assertEquals(Constants.MESSAGE_FORMATS_CONFIG_FILE, configurator.setFilename(Constants.MESSAGE_FORMATS_CONFIG_FILE))
        repository = ObjectRepositoryFactory().createObjectRepository(Constants.DEFAULT_OBJECT_REPOSITORY)
        self.assertEquals(repository, configurator.setObjectRepository(repository))
        
        configurator.loadConfiguration()
        configurator.createObjects()
        
        self.assertTrue(configurator.configureObject(FormatFactory()))
        factory = configurator.configureObject(FormatFactory())
        self.assertEquals(JSONFormat, factory.createMessageFormat(Constants.JSON).__class__)
    
    def test_try_configure_none_object(self):
        conf = FormatFactoryConfigurator()
        self.assertRaises(TypeError, conf.configureObject, None)
        
    def test_try_configure_non_hardware_dto_factory_object(self):
        conf = FormatFactoryConfigurator()
        self.assertRaises(TypeError, conf.configureObject, 1)