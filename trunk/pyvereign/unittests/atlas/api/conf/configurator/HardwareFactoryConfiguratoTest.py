from atlas.api.conf.configurator.HardwareFactoryConfigurator import HardwareFactoryConfigurator
from atlas.api.conf.repository.DefaultObjectRepository import DefaultObjectRepository
from json import ReadException
from atlas.api.env.hardware.HardwareFactory import HardwareFactory
import unittest

class HardwareFactoryConfiguratorTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(HardwareFactoryConfigurator())
    
    def test_load_configuration(self):
        configurator = HardwareFactoryConfigurator()
        self.assertEquals("hardwares.yaml", configurator.setFilename("hardwares.yaml"))
        repository = DefaultObjectRepository()
        self.assertEquals(repository, configurator.setObjectRepository(repository))
        self.assertTrue(configurator.loadConfiguration())
        self.assertTrue(configurator.getConfiguration())
    
    def test_load_invalid_configuration(self):
        configurator = HardwareFactoryConfigurator()
        self.assertEquals("invalidConf.yaml", configurator.setFilename("invalidConf.yaml"))
        repository = DefaultObjectRepository()
        self.assertEquals(repository, configurator.setObjectRepository(repository))
        self.assertRaises(ReadException, configurator.loadConfiguration)
        
    def test_try_load_configuration_invalid_filename(self):
        configurator = HardwareFactoryConfigurator()
        self.assertEquals("hard.yaml", configurator.setFilename("hard.yaml"))
        repository = DefaultObjectRepository()
        self.assertEquals(repository, configurator.setObjectRepository(repository))
        self.assertRaises(IOError, configurator.loadConfiguration)
    
    def test_try_set_none_filename(self):
        self.assertRaises(RuntimeError, HardwareFactoryConfigurator().setFilename, None)
        
    def test_try_set_non_string_value_in_set_filename_method(self):
        self.assertRaises(TypeError, HardwareFactoryConfigurator().setFilename, 1111)
    
    def test_try_set_empty_string_value_filename(self):
        self.assertRaises(RuntimeError, HardwareFactoryConfigurator().setFilename, "")
        
    def test_try_set_none_value_in_setObjectRepository_method(self):
        self.assertRaises(RuntimeError, HardwareFactoryConfigurator().setObjectRepository, None)
        
    def test_try_set_object_with_diferent_type_in_setObjectRepository_method(self):
        self.assertRaises(TypeError, HardwareFactoryConfigurator().setObjectRepository, "test")
        
    def test_create_objects(self):
        configurator = HardwareFactoryConfigurator()
        self.assertEquals("hardwares.yaml", configurator.setFilename("hardwares.yaml"))
        repository = DefaultObjectRepository()
        self.assertEquals(repository, configurator.setObjectRepository(repository))
        self.assertTrue(configurator.loadConfiguration())
        self.assertTrue(configurator.getConfiguration())
        self.assertTrue(configurator.createObjects())
        
    def test_configure_object_with_default_configuration(self):
        configurator = HardwareFactoryConfigurator()
        self.assertEquals("hardwares.yaml", configurator.setFilename("hardwares.yaml"))
        repository = DefaultObjectRepository()
        self.assertEquals(repository, configurator.setObjectRepository(repository))
        self.assertTrue(configurator.loadConfiguration())
        self.assertTrue(configurator.getConfiguration())
        self.assertTrue(configurator.createObjects())
        factory = HardwareFactory()
        self.assertEquals(factory, configurator.configureObject(factory, "default"))