from org.pyvereign.core.id.CoreServiceID import CoreServiceID
import unittest

class CoreServiceIDTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(CoreServiceID("test"))
        
    def test_getIDFormated(self):
        self.assertTrue(CoreServiceID("test").getIDFormat().find("urn:pyvereign:core:") >= 0)
        
        