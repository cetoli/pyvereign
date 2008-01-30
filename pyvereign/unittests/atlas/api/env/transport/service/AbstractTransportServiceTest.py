from atlas.api.env.transport.service.AbstractTransportService import AbstractTransportService
import unittest

class AbstractTransportServiceTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, AbstractTransportService)