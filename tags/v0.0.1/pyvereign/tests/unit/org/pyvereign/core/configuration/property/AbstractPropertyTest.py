from org.pyvereign.core.configuration.property.AbstractProperty import AbstractProperty
import unittest

class AbstractPropertyTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, AbstractProperty)