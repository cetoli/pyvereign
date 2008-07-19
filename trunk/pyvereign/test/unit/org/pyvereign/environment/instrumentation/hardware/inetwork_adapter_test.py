from org.pyvereign.environment.instrumentation.hardware.inetwork_adapter import INetworkAdapter
import unittest

class INetworkAdapterTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, INetworkAdapter)