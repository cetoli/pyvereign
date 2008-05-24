from org.pyvereign.core.platform.Module import Module
import unittest

class ModuleTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, Module)