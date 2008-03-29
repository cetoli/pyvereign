from org.pyvereign.core.environment.dto.system.AbstractProcess import AbstractProcess
import unittest

class AbstractProcessTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, AbstractProcess)