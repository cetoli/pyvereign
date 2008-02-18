from atlas.api.com.endpoint.service.EndpointService import EndpointService
import unittest

class EndpointServiceTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, EndpointService)