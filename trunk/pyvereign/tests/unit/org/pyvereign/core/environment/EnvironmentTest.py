from org.pyvereign.core.environment.Environment import Environment
from org.pyvereign.core.environment.DefaultTransportService import DefaultTransportService
from org.pyvereign.core.id.IDFactory import IDFactory
from org.pyvereign.core.microkernel.CoreServiceRequest import CoreServiceRequest
import unittest

class EnvironmentTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(Environment())
        
   