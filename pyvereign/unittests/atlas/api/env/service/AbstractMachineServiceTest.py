from atlas.api.env.service.AbstractMachineService import AbstractMachineService
import unittest

class AbstractMachineServiceTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, AbstractMachineService)