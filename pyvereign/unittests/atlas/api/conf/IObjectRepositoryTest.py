from atlas.api.conf.repository.ObjectRepository import ObjectRepository
import unittest

class IObjectRepositoryTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, ObjectRepository)