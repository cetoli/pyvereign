from atlas.api.conf.property.DefaultProperty import DefaultProperty
from atlas.api.conf.repository.DefaultObjectRepository import DefaultObjectRepository
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
    
    