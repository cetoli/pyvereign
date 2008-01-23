from atlas.api.conf.property.DefaultProperty import DefaultProperty
import unittest

class DefaultPropertyTest(unittest.TestCase):
    
    def test_create_default_property(self):
        property = DefaultProperty("test", "testing")
        self.assertEquals("test", property.getName())
        self.assertEquals("testing", property.getValue())
        self.assertEquals(0, property.getNumberOfProperties())
        self.assertFalse(property.isComposite())
    
    def test_try_add_property(self):
        property = DefaultProperty("test", "testing")
        self.assertRaises(RuntimeError, property.addProperty, DefaultProperty("ha", "ole"))
        self.assertFalse(property.hasProperty("ha"))
        self.assertEquals(0, property.getNumberOfProperties())
    
    def test_try_remove_property(self):
        property = DefaultProperty("test", "testing")
        self.assertRaises(RuntimeError, property.addProperty, DefaultProperty("ha", "ole"))
        self.assertFalse(property.hasProperty("ha"))
        self.assertEquals(0, property.getNumberOfProperties())
        self.assertRaises(RuntimeError, property.removeProperty, "ha")
        self.assertEquals(0, property.getNumberOfProperties())
    
    def test_try_get_property(self):
        property = DefaultProperty("test", "testing")
        self.assertRaises(RuntimeError, property.addProperty, DefaultProperty("ha", "ole"))
        self.assertFalse(property.hasProperty("ha"))
        self.assertEquals(0, property.getNumberOfProperties())
        self.assertRaises(RuntimeError, property.getProperty, "ha")