from org.pyvereign.core.microkernel.Microkernel import Microkernel
import unittest

class MicrokernelTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertEquals(Microkernel(), Microkernel())