from atlas.api.env.system.commapi.AbstractCommunicationAPIAdapter import AbstractCommunicationAPIAdapter
import unittest

class AbstractCmmunicationAPITest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, AbstractCommunicationAPIAdapter)