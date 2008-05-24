from org.pyvereign.core.environment.service.NetworkingService import NetworkingService
import unittest

class NetworkingServiceTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, NetworkingService)