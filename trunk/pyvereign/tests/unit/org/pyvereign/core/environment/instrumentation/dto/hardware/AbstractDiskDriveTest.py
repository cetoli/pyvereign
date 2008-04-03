from org.pyvereign.core.environment.instrumentation.dto.hardware.AbstractDiskDrive import AbstractDiskDrive
import unittest

class AbstractDiskDriveTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, AbstractDiskDrive)