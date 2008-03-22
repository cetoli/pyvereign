from org.pyvereign.core.platform.CoreService import CoreService
import unittest

class CoreServiceTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, CoreService)