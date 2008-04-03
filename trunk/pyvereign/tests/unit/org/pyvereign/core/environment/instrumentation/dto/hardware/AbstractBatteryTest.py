from org.pyvereign.core.environment.instrumentation.dto.hardware.AbstractBattery import AbstractBattery
import unittest

class AbstractBatteryTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, AbstractBattery)