from atlas.api.env.system.commapi.CommunicationAPI import CommunicationAPI 
import unittest

class CommunicationAPITest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, CommunicationAPI)