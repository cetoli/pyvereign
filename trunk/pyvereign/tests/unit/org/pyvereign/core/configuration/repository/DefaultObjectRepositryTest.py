from org.pyvereign.core.configuration.repository.DefaultObjectRepository import DefaultObjectRepository
from org.pyvereign.core.configuration.property.DefaultProperty import DefaultProperty
import unittest

class DefaultObjectRepositoryTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(DefaultObjectRepository())
    
    def test_add_object_in_repository(self):
        rep = DefaultObjectRepository()
        prop = DefaultProperty("test", 123)
        self.assertEquals(prop, rep.addObject("test", prop))
        self.assertEquals(1, rep.getNumberOfObjects())
        self.assertEquals(prop, rep.getObject("test"))
    
    def test_remove_object_from_repository(self):
        rep = DefaultObjectRepository()
        prop = DefaultProperty("test", 123)
        self.assertEquals(prop, rep.addObject("test", prop))
        self.assertEquals(1, rep.getNumberOfObjects())
        self.assertEquals(prop, rep.getObject("test"))
        
        self.assertEquals(prop, rep.removeObject("test"))
        self.assertEquals(0, rep.getNumberOfObjects())
    
    def test_try_add_object_with_none_name(self):
        rep = DefaultObjectRepository()
        self.assertRaises(RuntimeError, rep.addObject, None, "test")
    
    def test_try_add_object_with_non_sring_instance_in_name_parameter(self):
        rep = DefaultObjectRepository()
        self.assertRaises(TypeError, rep.addObject, 111, "test")
    
    def test_try_add_none_object(self):
        self.assertRaises(RuntimeError, DefaultObjectRepository().addObject, "test", None)
        
    def test_try_remove_with_none_name(self):
        self.assertRaises(RuntimeError, DefaultObjectRepository().removeObject, None)
        
    def test_try_remove_non_existent_object(self):
        self.assertRaises(KeyError, DefaultObjectRepository().removeObject, "test")
        
    def test_try_remove_non_string_instance_in_name_parameter(self):
        self.assertRaises(TypeError, DefaultObjectRepository().removeObject, 222)
        
    def test_try_getObject_with_none_name(self):
        self.assertRaises(RuntimeError, DefaultObjectRepository().getObject, None)
        
    def test_try_getObject_non_existent_object(self):
        self.assertRaises(KeyError, DefaultObjectRepository().getObject, "test")
        
    def test_try_getObject_non_string_instance_in_name_parameter(self):
        self.assertRaises(TypeError, DefaultObjectRepository().getObject, 222)
        
    def test_has_object_with_none_name(self):
        self.assertRaises(RuntimeError, DefaultObjectRepository().hasObject, None)
        
    def test_has_object_non_existent_object(self):
        self.assertFalse(DefaultObjectRepository().hasObject("test"))
        
    def test_has_object_non_string_instance_in_name_parameter(self):
        self.assertRaises(TypeError, DefaultObjectRepository().hasObject, 222)