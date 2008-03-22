from org.pyvereign.core.platform.Service import Service
import unittest

class ServiceTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, Service)