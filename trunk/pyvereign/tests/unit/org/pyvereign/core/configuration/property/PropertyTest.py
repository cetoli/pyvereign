from org.pyvereign.core.configuration.property.Property import Property
import unittest

class IPropertyTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, Property)