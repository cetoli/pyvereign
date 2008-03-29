from org.pyvereign.core.environment.dto.hardware.Processor import Processor
import unittest

class ProcessorTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, Processor)