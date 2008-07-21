from org.pyvereign.environment.instrumentation.hardware.iphysical_memory import IPhysicalMemory
import unittest

class IPhysicalMemoryTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, IPhysicalMemory)