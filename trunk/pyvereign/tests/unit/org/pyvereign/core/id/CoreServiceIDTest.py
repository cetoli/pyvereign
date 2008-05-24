from org.pyvereign.core.id.CoreServiceID import CoreServiceID
from org.pyvereign.util.Constants import Constants
import unittest

class CoreServiceIDTest(unittest.TestCase):
    
    def test_create_instance_with_environment_networking(self):
        self.assertTrue(CoreServiceID(Constants.ENVIRONMENT, Constants.NETWORKING_SERVICE))
        id = CoreServiceID(Constants.ENVIRONMENT, Constants.NETWORKING_SERVICE)
        self.assertTrue(id.getIDFormated().find("urn:pyvereign:core:service:") >= 0)
    
    def test_create_instance_with_environment_transport(self):
        self.assertTrue(CoreServiceID(Constants.ENVIRONMENT, Constants.TRANSPORT_SERVICE))
        id = CoreServiceID(Constants.ENVIRONMENT, Constants.TRANSPORT_SERVICE)
        self.assertTrue(id.getIDFormated().find("urn:pyvereign:core:service:") >= 0)
