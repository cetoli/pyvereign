from atlas.api.conf.property.CompositeProperty import CompositeProperty
from atlas.api.conf.property.DefaultProperty import DefaultProperty
import unittest

class CompositePropertyTest(unittest.TestCase):
    
    def test_create_a_composite_property(self):
        property = CompositeProperty("windows")
        self.assertEquals("windows", property.getName())
    
    def test_try_set_value_in_property(self):
        property = CompositeProperty("value")
        self.assertRaises(RuntimeError, property.setValue, 10)
        
    def test_try_get_value_of_a_property(self):
        property = CompositeProperty("value")
        self.assertRaises(RuntimeError, property.setValue, 10)
        self.assertRaises(RuntimeError, property.getValue)
        
    def test_set_name(self):
        property = CompositeProperty("windows")
        self.assertEquals("windows", property.getName())
        
        property.setName("linux")
        self.assertEquals("linux", property.getName())
        
    def test_add_one_property(self):
        property = CompositeProperty("windows")
        self.assertEquals("windows", property.getName())
        module = DefaultProperty("module", "atlas")
        self.assertEquals(module, property.addProperty(module))
        self.assertEquals(1, property.getNumberOfProperties())
        self.assertTrue(property.hasProperty("module"))
        self.assertEquals(1, len(property.getProperties()))
    
    def test_auto_reference(self):
        property = CompositeProperty("windows")
        self.assertRaises(RuntimeError, property.addProperty, property)
        
    def test_set_level(self):
        property = CompositeProperty("windows")
        module = DefaultProperty("module", "atlas")
        classname = DefaultProperty("classname", "Windows")
        self.assertEquals(module, property.addProperty(module))
        self.assertEquals(classname, property.addProperty(classname))
        self.assertEquals(2, property.getNumberOfProperties())
        self.assertEquals(2, len(property.getProperties()))
        self.assertEquals(module, property.removeProperty("module"))
        self.assertEquals(1, len(property.getProperties()))
        self.assertEquals(1, property.getNumberOfProperties())
        self.assertEquals(classname, property.getProperty("classname"))
        property.setLevel(1)
        self.assertEquals(1, module.getLevel())
        self.assertEquals(2, classname.getLevel())
    
    def test_add_two_properties_and_remove_one(self):
        property = CompositeProperty("windows")
        module = DefaultProperty("module", "atlas")
        classname = DefaultProperty("classname", "Windows")
        self.assertEquals(module, property.addProperty(module))
        self.assertEquals(classname, property.addProperty(classname))
        self.assertEquals(2, property.getNumberOfProperties())
        self.assertEquals(2, len(property.getProperties()))
        self.assertEquals(module, property.removeProperty("module"))
        self.assertEquals(1, len(property.getProperties()))
        self.assertEquals(1, property.getNumberOfProperties())
        self.assertEquals(classname, property.getProperty("classname"))
    
    def test_try_get_non_existent_property(self):
        property = CompositeProperty("linux")
        self.assertRaises(KeyError, property.getProperty, "platform")
    
    def test_add_composite_property(self):
        property = CompositeProperty("windows")
        device = CompositeProperty("device")
        memory = DefaultProperty("memory", 1024)
        disk = DefaultProperty("disk", 2048)
        self.assertEquals(memory, device.addProperty(memory))
        self.assertEquals(disk, device.addProperty(disk))
        self.assertEquals(device, property.addProperty(device))
        property.setLevel(1)
        self.assertEquals(1, property.getLevel())
        self.assertEquals(2, device.getLevel())
        self.assertEquals(3, memory.getLevel())
        self.assertEquals(3, disk.getLevel())
        self.assertEquals(1, property.getNumberOfProperties())