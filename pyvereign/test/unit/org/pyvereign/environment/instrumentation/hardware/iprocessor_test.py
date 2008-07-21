from org.pyvereign.environment.instrumentation.hardware.iprocessor import IProcessor
import unittest

class IProcessorTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, IProcessor)