from org.pyvereign.core.environment.instrumentation.dto.hardware.Battery import Battery
import unittest

class BatteryTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, Battery)