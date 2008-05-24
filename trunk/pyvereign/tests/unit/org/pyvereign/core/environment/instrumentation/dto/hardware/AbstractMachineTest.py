from org.pyvereign.core.environment.instrumentation.dto.hardware.AbstractMachine import AbstractMachine
import unittest

class AbstractMachineTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, AbstractMachine)