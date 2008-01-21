from atlas.api.conf.Configurator import Configurator
import unittest

class IConfiguratorTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, Configurator)