from atlas.api.conf.repository.AbstractObjectRepository import AbstractObjectRepository
import unittest

class AbstractObjectRepositoryTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, AbstractObjectRepository)