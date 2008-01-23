from atlas.api.env.hardware.HardwareFactory import HardwareFactory
from atlas.api.env.hardware.DefaultMachine import DefaultMachine
from atlas.api.conf.service.HardwareFactoryConfigurator import HardwareFactoryConfigurator
from atlas.api.conf.repository.DefaultObjectRepository import DefaultObjectRepository
import unittest

class HardwareFactoryConfiguratorTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(HardwareFactoryConfigurator())
    
    def test_load_configuration(self):
        configurator = HardwareFactoryConfigurator()
        configurator.setFilename("hardwares.yaml")
        configurator.setObjectRepository(DefaultObjectRepository())
        
        self.assertTrue(configurator.loadConfiguration())
        self.assertTrue(configurator.getConfiguration())
    
    def test_create_objects(self):
        configurator = HardwareFactoryConfigurator()
        configurator.setFilename("hardwares.yaml")
        configurator.setObjectRepository(DefaultObjectRepository())
        
        self.assertTrue(configurator.loadConfiguration())
        self.assertTrue(configurator.getConfiguration())
        
        self.assertTrue(configurator.createObjects())
        
    def test_configure_object(self):
        factory = HardwareFactory()
        
        configurator = HardwareFactoryConfigurator()
        configurator.setFilename("hardwares.yaml")
        configurator.setObjectRepository(DefaultObjectRepository())
        
        self.assertTrue(configurator.loadConfiguration())
        self.assertTrue(configurator.getConfiguration())
        
        self.assertTrue(configurator.createObjects())
        
        self.assertEquals(factory, configurator.configureObject(factory, "default"))
        
        self.assertEquals(DefaultMachine, factory.createHardware(HardwareFactory.MACHINE).__class__)