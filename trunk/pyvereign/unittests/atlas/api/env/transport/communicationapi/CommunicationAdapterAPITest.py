from atlas.api.env.transport.communicationapi.CommunicationAPIAdapter import CommunicationAPIAdapter
import unittest

class CommunicationAPIAdapterTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, CommunicationAPIAdapter)