from org.pyvereign.core.platform.CompositeModule import CompositeModule
import unittest

class CompositeModuleTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, CompositeModule)