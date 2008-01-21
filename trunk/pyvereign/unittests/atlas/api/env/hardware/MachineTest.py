from atlas.api.env.hardware.Machine import Machine
import unittest

class MachineTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, Machine)