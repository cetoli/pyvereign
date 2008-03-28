from org.pyvereign.core.platform.SimpleModule import SimpleModule
import unittest

class SimpleModuleTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, SimpleModule)