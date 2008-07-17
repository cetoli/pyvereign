from org.pyvereign.environment.instrumentation.hardware.abstract_hardware import AbstractHardware
from org.pyvereign.base.interface import implements
from org.pyvereign.environment.instrumentation.hardware.ihardware import IHardware
import unittest

class AbstractHardwareTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, AbstractHardware)
