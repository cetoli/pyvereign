from org.pyvereign.core.environment.instrumentation.dto.hardware.AbstractPhysicalMemory import AbstractPhysicalMemory
import unittest

class AbstractPhysicalMemoryTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, AbstractPhysicalMemory)