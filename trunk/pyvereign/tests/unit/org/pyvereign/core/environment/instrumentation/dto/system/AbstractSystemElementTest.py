from org.pyvereign.core.environment.instrumentation.dto.system.AbstractSystemElement import AbstractSystemElement
import unittest

class AbstractSystemElementTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, AbstractSystemElement)