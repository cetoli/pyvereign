from org.pyvereign.environment.instrumentation.dataaccess.ibattery_dao import IBatteryDAO
import unittest

class IBatteryDAOTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, IBatteryDAO)