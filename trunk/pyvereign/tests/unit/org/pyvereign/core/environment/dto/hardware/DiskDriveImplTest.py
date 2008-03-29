from org.pyvereign.core.environment.dto.hardware.DiskDriveImpl import DiskDriveImpl
from org.pyvereign.core.environment.dto.hardware.DiskDrive import DiskDrive
import unittest

class DiskDriveImplTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(DiskDriveImpl({}))
        
        values = {"description": "Hard Disk", "driveType": 3, "fileSystem": "NTFS",
                  "freeSpace": 81000, "hardwareId": "123", "logicalName": "Local Disk",
                  "product": "Hard Disk", "serial": "fff", "size": 1200000, 
                  "vendor": "Sansung", "volumeName": "Local Disk"}
        
        drive = DiskDriveImpl(values)
        self.assertEquals("Hard Disk", drive.getDescription())
        self.assertEquals(DiskDrive.TYPE_LOCAL_DISK, drive.getDriveType())
        self.assertEquals("NTFS", drive.getFileSystem())
        self.assertEquals(81000, drive.getFreeSpace())
        self.assertEquals("123", drive.getHardwareId())
        self.assertEquals("Local Disk", drive.getLogicalName())
        self.assertEquals("Hard Disk", drive.getProduct())
        self.assertEquals("fff", drive.getSerial())
        self.assertEquals(1200000, drive.getSize())
        self.assertEquals("Sansung", drive.getVendor())
        self.assertEquals("Local Disk", drive.getVolumeName())
        
    def test_try_create_instance(self):
        self.assertRaises(RuntimeError, DiskDriveImpl, {"test": "test"})