from atlas.api.env.transport.service.TransportService import TransportService 
import unittest

class TransportServiceTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, TransportService)