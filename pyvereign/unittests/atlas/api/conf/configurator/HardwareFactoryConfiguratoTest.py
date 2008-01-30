from atlas.api.conf.configurator.HardwareFactoryConfigurator import HardwareFactoryConfigurator
from atlas.api.conf.repository.DefaultObjectRepository import DefaultObjectRepository
import unittest

class HardwareFactoryConfiguratorTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(HardwareFactoryConfigurator())
    
    def test_load_default_configuration(self):
        configurator = HardwareFactoryConfigurator()
        self.assertEquals("hardwares.yaml", configurator.setFilename("hardwares.yaml"))
        repository = DefaultObjectRepository()
        self.assertEquals(repository, configurator.setObjectRepository(repository))
        self.assertTrue(configurator.loadConfiguration())
        self.assertTrue(configurator.getConfiguration())
        
    def test_try_load_configuration_invalid_filename(self):
        configurator = HardwareFactoryConfigurator()
        self.assertEquals("hard.yaml", configurator.setFilename("hard.yaml"))
        repository = DefaultObjectRepository()
        self.assertEquals(repository, configurator.setObjectRepository(repository))
        self.assertRaises(IOError, configurator.loadConfiguration)
    
