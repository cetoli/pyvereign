from org.pyvereign.environment.instrumentation.hardware.ihardware import IHardware
import unittest

class IHardwareTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, IHardware)