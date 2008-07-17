from org.pyvereign.environment.instrumentation.hardware.idisk_drive import IDiskDrive
import unittest

class IDiskDriveTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, IDiskDrive)