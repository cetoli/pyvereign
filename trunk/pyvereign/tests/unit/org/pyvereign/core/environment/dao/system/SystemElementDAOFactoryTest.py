from org.pyvereign.core.environment.dao.system.SystemElementDAOFactory import SystemElementDAOFactory
import unittest

class SystemElementDAOFactoryTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, SystemElementDAOFactory)