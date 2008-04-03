from org.pyvereign.core.environment.instrumentation.dao.system.ProcessDAO import ProcessDAO
import unittest

class ProcessDAOTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, ProcessDAO)