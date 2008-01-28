from atlas.api.env.EnvironmentService import EnvironmentService
import unittest

class EnvironmentServiceTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, EnvironmentService)