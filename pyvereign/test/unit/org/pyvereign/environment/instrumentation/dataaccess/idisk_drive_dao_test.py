from org.pyvereign.environment.instrumentation.dataaccess.idisk_drive_dao import IDiskDriveDAO
import unittest

class IDiskDriveDAOTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, IDiskDriveDAO)