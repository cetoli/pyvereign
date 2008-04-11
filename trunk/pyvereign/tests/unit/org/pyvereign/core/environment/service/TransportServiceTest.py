from org.pyvereign.core.environment.service.TranportService import TransportService
import unittest

class TransportListenerTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, TransportService)