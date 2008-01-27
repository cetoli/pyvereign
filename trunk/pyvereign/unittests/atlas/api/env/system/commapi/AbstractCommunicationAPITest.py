from atlas.api.env.system.commapi.AbstractCommunicationAPI import AbstractCommunicationAPI 
import unittest

class AbstractCmmunicationAPITest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, AbstractCommunicationAPI)