from atlas.api.microkernel.Microkernel import Microkernel
from atlas.api.env.hardware.HardwareFactory import HardwareFactory
import unittest

class MicrokernelTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(Microkernel())
    
    def test_configure_hardware_factory(self):
        factory = HardwareFactory()
        Microkernel().initialize()
        Microkernel().start()
        self.assertEquals(factory, Microkernel().executeMecanism("InternalConfiguration", "configurator", "configureHardwareFactory", factory, "default"))
        
        self.assertTrue(factory.createHardware(HardwareFactory.MACHINE))
