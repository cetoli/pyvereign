from org.pyvereign.core.environment.EnvironmentConfigurator import EnvironmentConfigurator
from org.pyvereign.util.Constants import Constants
from org.pyvereign.core.configuration.repository.ObjectRepositoryFactory import ObjectRepositoryFactory
from org.pyvereign.core.environment.Environment import Environment
import unittest

class EnvironmentConfiguratorTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(EnvironmentConfigurator())
        
    def test_load_configuration_create_objects(self):
        configurator = EnvironmentConfigurator()
        self.assertEquals(Constants.ENVIRONMENT_CONFIG_FILE, configurator.setFilename(Constants.ENVIRONMENT_CONFIG_FILE))
        repository = ObjectRepositoryFactory().createObjectRepository(Constants.DEFAULT_OBJECT_REPOSITORY)
        self.assertEquals(repository, configurator.setObjectRepository(repository))
        
        configurator.loadConfiguration()
        configurator.createObjects()
        
        self.assertTrue(repository.getObject(Constants.NETWORKING_SERVICE))
        self.assertTrue(repository.getObject(Constants.TRANSPORT_SERVICE))
    
    def test_configure_object(self):
        configurator = EnvironmentConfigurator()
        self.assertEquals(Constants.ENVIRONMENT_CONFIG_FILE, configurator.setFilename(Constants.ENVIRONMENT_CONFIG_FILE))
        repository = ObjectRepositoryFactory().createObjectRepository(Constants.DEFAULT_OBJECT_REPOSITORY)
        self.assertEquals(repository, configurator.setObjectRepository(repository))
        
        configurator.loadConfiguration()
        configurator.createObjects()
        
        self.assertTrue(configurator.configureObject(Environment()))
        
        environment = configurator.configureObject(Environment())
        self.assertEquals(2, environment.countModules())
    
    def test_try_configure_non_environment_object(self):
        self.assertRaises(TypeError, EnvironmentConfigurator().configureObject, "environment")
    
    def test_try_configure_object_with_none_obj(self):
        self.assertRaises(TypeError, EnvironmentConfigurator().configureObject, None)
        
        
        
        