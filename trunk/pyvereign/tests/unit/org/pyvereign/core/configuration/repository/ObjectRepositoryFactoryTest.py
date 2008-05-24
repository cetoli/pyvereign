from org.pyvereign.core.configuration.repository.ObjectRepositoryFactory import ObjectRepositoryFactory
from org.pyvereign.util.Constants import Constants
from org.pyvereign.core.configuration.repository.DefaultObjectRepository import DefaultObjectRepository
import unittest

class ObjectRepositoryFactoryTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(ObjectRepositoryFactory())
        self.assertEquals(ObjectRepositoryFactory(), ObjectRepositoryFactory())
    
    def test_create_default_object_repository(self):
        self.assertTrue(ObjectRepositoryFactory().createObjectRepository(Constants.DEFAULT_OBJECT_REPOSITORY))
        self.assertEquals(DefaultObjectRepository, ObjectRepositoryFactory().createObjectRepository(Constants.DEFAULT_OBJECT_REPOSITORY).__class__)