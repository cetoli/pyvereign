from atlas.api.env.Environment import Environment
from atlas.api.microkernel.Microkernel import Microkernel
from atlas.api.env.hardware.HardwareFactory import HardwareFactory
import unittest

class EnvironmentTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(Environment())
    
    def test_environment_machine_getname(self):
        Microkernel().initialize()
        Microkernel().start()
        Microkernel().executeMecanism("InternalConfiguration", "configurator", "configureHardwareFactory", HardwareFactory(), "default")
        environment = Environment()
        environment.initialize()
        environment.start()
        
        self.assertEquals("COVERDALE", environment.executeService("machine", "getLogicalName"))