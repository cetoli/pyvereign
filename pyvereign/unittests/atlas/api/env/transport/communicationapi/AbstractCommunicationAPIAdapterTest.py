from atlas.api.env.transport.communicationapi.AbstractCommunicationAPI import AbstractCommunicationAPIAdapter
import unittest

class AbstractCommunicationAPIAdapterTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, AbstractCommunicationAPIAdapter)