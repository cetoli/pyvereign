from atlas.api.com.AbstractCommunicationService import AbstractCommunicationService
import unittest

class AbstractCommunicationServiceTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, AbstractCommunicationService)