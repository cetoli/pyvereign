from org.pyvereign.environment.instrumentation.hardware.imachine import IMachine
import unittest

class IMachineTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, IMachine)