from atlas.api.env.service.MachineService import MachineService
import unittest

class MachineServiceTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, MachineService)