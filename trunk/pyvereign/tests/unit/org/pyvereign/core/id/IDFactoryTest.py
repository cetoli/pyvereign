from org.pyvereign.core.id.IDFactory import IDFactory
from org.pyvereign.core.id.CoreServiceID import CoreServiceID
from org.pyvereign.util.Constants import Constants
import unittest

class IDFactoryTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(IDFactory())
        self.assertEquals(IDFactory(), IDFactory())
        
    