from org.pyvereign.core.environment.dto.hardware.AbstractProcessor import AbstractProcessor
import unittest

class AbstractProcessorTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, AbstractProcessor)