from atlas.api.microkernel.Microkernel import Microkernel
import unittest

class MicrokernelTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(Microkernel())
    
    def test_environment_machine_getLogicalName(self):
        Microkernel().initialize()
        Microkernel().start()
        
        self.assertEquals("COVERDALE", Microkernel().executeMecanism("Environment", "machine", "getLogicalName"))
        
