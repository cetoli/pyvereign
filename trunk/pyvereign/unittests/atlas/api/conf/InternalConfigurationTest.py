from atlas.api.conf.InternalConfiguration import InternalConfiguration
from atlas.api.env.hardware.HardwareFactory import HardwareFactory
import unittest

class InternalConfigurationTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(InternalConfiguration())
    
    def test_configure_hardware_factory(self):
        layer = InternalConfiguration()
        layer.initialize()
        layer.start()
        factory = HardwareFactory()
        self.assertEquals(factory, layer.executeService("configurator", "configureHardwareFactory", factory, "default"))