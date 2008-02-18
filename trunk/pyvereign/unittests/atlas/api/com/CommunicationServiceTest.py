from atlas.api.com.CommunicationService import CommunicationService
import unittest

class CommunicationServiceTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, CommunicationService)