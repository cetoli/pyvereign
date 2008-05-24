from org.pyvereign.core.environment.instrumentation.dto.hardware.PhysicalMemory import PhysicalMemory
import unittest

class PhysicalMemoryTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, PhysicalMemory)