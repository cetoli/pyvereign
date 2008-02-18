from atlas.api.com.endpoint.service.DefaultEndpointService import DefaultEndpointService
import unittest

class DefaultEndpointServiceTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(DefaultEndpointService())