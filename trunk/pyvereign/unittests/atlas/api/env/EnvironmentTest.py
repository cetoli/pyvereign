from atlas.api.env.Environment import Environment
import unittest

class EnvironmentTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(Environment())
    
    def test_environment_machine_getname(self):
        environment = Environment()
        environment.initialize()
        environment.start()
        
        self.assertEquals("COVERDALE", environment.executeService("machine", "getLogicalName"))