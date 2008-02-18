from atlas.api.com.endpoint.service.AbstractEndpointService import AbstractEndpointService
import unittest

class AbstractEndpointServiceTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, AbstractEndpointService)