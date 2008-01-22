import unittest
from atlas.api.microkernel.InternalServer import InternalServer

class InternalServerTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, InternalServer)