from org.pyvereign.core.platform.AbstractService import AbstractService
import unittest

class AbstractServiceTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, AbstractService)