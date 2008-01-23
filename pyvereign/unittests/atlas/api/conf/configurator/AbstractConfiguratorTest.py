from atlas.api.conf.configurator.AbstractConfigurator import AbstractConfigurator
import unittest

class AbstractConfiguatorTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, AbstractConfigurator)