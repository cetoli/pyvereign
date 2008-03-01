from atlas.api.com.ipc.service.DefaultIPCService import DefaultIPCService
import unittest

class DefaultIPCServiceTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(DefaultIPCService())