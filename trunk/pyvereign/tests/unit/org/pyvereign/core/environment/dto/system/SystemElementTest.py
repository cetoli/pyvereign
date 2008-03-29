from org.pyvereign.core.environment.dto.system.SystemElement import SystemElement
import unittest

class SystemElementTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, SystemElement)