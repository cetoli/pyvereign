from atlas.api.env.AbstractEnvironmentService import AbstractEnvironmentService
import unittest

class AbstractEnvironmentServiceTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, AbstractEnvironmentService)