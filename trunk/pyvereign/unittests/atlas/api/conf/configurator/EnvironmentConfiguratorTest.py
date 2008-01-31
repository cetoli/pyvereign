from atlas.api.conf.configurator.EnvironmentConfigurator import EnvironmentConfigurator
from atlas.api.conf.repository.DefaultObjectRepository import DefaultObjectRepository
from json import ReadException
from atlas.api.env.Environment import Environment
import unittest

class EnvironmentConfiguratorTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(EnvironmentConfigurator())
        
    def test_load_configuration(self):
        configurator = EnvironmentConfigurator()
        self.assertEquals("environment.yaml", configurator.setFilename("environment.yaml"))
        repository = DefaultObjectRepository()
        self.assertEquals(repository, configurator.setObjectRepository(repository))
        self.assertTrue(configurator.loadConfiguration())
        self.assertTrue(configurator.getConfiguration())
    
    def test_load_invalid_configuration(self):
        configurator = EnvironmentConfigurator()
        self.assertEquals("invalidConf.yaml", configurator.setFilename("invalidConf.yaml"))
        repository = DefaultObjectRepository()
        self.assertEquals(repository, configurator.setObjectRepository(repository))
        self.assertRaises(ReadException, configurator.loadConfiguration)
        
    def test_try_load_configuration_invalid_filename(self):
        configurator = EnvironmentConfigurator()
        self.assertEquals("env.yaml", configurator.setFilename("env.yaml"))
        repository = DefaultObjectRepository()
        self.assertEquals(repository, configurator.setObjectRepository(repository))
        self.assertRaises(IOError, configurator.loadConfiguration)
    
    def test_try_set_none_filename(self):
        self.assertRaises(RuntimeError, EnvironmentConfigurator().setFilename, None)
        
    def test_try_set_non_string_value_in_set_filename_method(self):
        self.assertRaises(TypeError, EnvironmentConfigurator().setFilename, 1111)
    
    def test_try_set_empty_string_value_filename(self):
        self.assertRaises(RuntimeError, EnvironmentConfigurator().setFilename, "")
        
    def test_try_set_none_value_in_setObjectRepository_method(self):
        self.assertRaises(RuntimeError, EnvironmentConfigurator().setObjectRepository, None)
        
    def test_try_set_object_with_diferent_type_in_setObjectRepository_method(self):
        self.assertRaises(TypeError, EnvironmentConfigurator().setObjectRepository, "test")
        
    def test_create_objects(self):
        configurator = EnvironmentConfigurator()
        self.assertEquals("environment.yaml", configurator.setFilename("environment.yaml"))
        repository = DefaultObjectRepository()
        self.assertEquals(repository, configurator.setObjectRepository(repository))
        self.assertTrue(configurator.loadConfiguration())
        self.assertTrue(configurator.getConfiguration())
        self.assertTrue(configurator.createObjects())
    
    def test_configure_object_with_nt_configuration(self):
        configurator = EnvironmentConfigurator()
        self.assertEquals("environment.yaml", configurator.setFilename("environment.yaml"))
        repository = DefaultObjectRepository()
        self.assertEquals(repository, configurator.setObjectRepository(repository))
        self.assertTrue(configurator.loadConfiguration())
        self.assertTrue(configurator.getConfiguration())
        self.assertTrue(configurator.createObjects())
        environment = Environment()
        environment.initialize()
        self.assertEquals(environment, configurator.configureObject(environment, "nt"))