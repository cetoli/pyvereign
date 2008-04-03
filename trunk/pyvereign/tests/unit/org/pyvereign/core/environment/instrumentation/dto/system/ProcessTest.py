from org.pyvereign.core.environment.instrumentation.dto.system.Process import Process
import unittest

class ProcessTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, Process)