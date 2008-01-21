from atlas.api.env.service.DefaultMachineService import DefaultMachineService
import unittest

class DefaultMachineTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(DefaultMachineService())