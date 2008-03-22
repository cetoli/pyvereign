from org.pyvereign.core.platform.AbstractModule import AbstractModule
import unittest

class AbsractModuleTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, AbstractModule)