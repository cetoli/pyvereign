from org.pyvereign.environment.instrumentation.hardware.ibattery import IBattery
import unittest

class IBatteryTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, IBattery)