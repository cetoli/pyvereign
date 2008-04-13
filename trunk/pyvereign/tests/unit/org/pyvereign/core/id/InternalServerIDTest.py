from org.pyvereign.core.id.InternalServerID import InternalServerID
from org.pyvereign.util.Constants import Constants
import unittest

class InternalServerIDTest(unittest.TestCase):
    
    def test_create_instance_with_environment(self):
        self.assertTrue(InternalServerID(Constants.ENVIRONMENT))
        id = InternalServerID(Constants.ENVIRONMENT)
        self.assertTrue(id.getIDFormated().find("urn:pyvereign:core:internalserver:") == 0)