from org.pyvereign.core.id.ID import ID
import unittest

class IDTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, ID)