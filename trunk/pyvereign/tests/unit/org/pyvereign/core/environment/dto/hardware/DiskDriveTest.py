from org.pyvereign.core.environment.dto.hardware.DiskDrive import DiskDrive
import unittest

class DiskDriveTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, DiskDrive)