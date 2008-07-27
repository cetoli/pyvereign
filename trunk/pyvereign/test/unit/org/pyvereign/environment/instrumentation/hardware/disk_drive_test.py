from org.pyvereign.environment.instrumentation.hardware.idisk_drive import IDiskDrive
from org.pyvereign.base.interface import implements
from org.pyvereign.environment.instrumentation.hardware.disk_drive import DiskDrive
from org.pyvereign.environment.instrumentation.hardware.ihardware import IHardware
from org.pyvereign.error.illegal_argument_error import IllegalArgumentError
from org.pyvereign.environment.instrumentation.hardware.idisk_drive_constants import IDiskDriveConstants
import unittest

class DiskDriveTest(unittest.TestCase):
    
    def setUp(self):
        self.drive = DiskDrive()
    
    def test_create_instance(self):
        self.assertTrue(DiskDrive())
        drive = DiskDrive()
        self.assertEquals(IDiskDriveConstants.TYPE_LOCAL_DISK, drive.getDriveType())
        self.assertEquals("", drive.getFileSystem())
        self.assertEquals(0, drive.getFreeSpace())
        self.assertEquals(0, drive.getSize())
        self.assertEquals("", drive.getVolumeName())
        self.assertTrue(implements(drive, IHardware, IDiskDrive))
        
    def test_set_get_drive_type(self):
        self.assertEquals(IDiskDriveConstants.TYPE_UNKNOW, self.drive.setDriveType(0))
        self.assertEquals(IDiskDriveConstants.TYPE_UNKNOW, self.drive.getDriveType())
        self.assertEquals(IDiskDriveConstants.TYPE_NO_ROOT_DIRECTORY, self.drive.setDriveType(1))
        self.assertEquals(IDiskDriveConstants.TYPE_NO_ROOT_DIRECTORY, self.drive.getDriveType())
        self.assertEquals(IDiskDriveConstants.TYPE_REMOVABLE_DRIVE, self.drive.setDriveType(2))
        self.assertEquals(IDiskDriveConstants.TYPE_REMOVABLE_DRIVE, self.drive.getDriveType())
        self.assertEquals(IDiskDriveConstants.TYPE_LOCAL_DISK, self.drive.setDriveType(3))
        self.assertEquals(IDiskDriveConstants.TYPE_LOCAL_DISK, self.drive.getDriveType())
        self.assertEquals(IDiskDriveConstants.TYPE_NETWORK_DRIVE, self.drive.setDriveType(4))
        self.assertEquals(IDiskDriveConstants.TYPE_NETWORK_DRIVE, self.drive.getDriveType())
        self.assertEquals(IDiskDriveConstants.TYPE_COMPACT_DISK, self.drive.setDriveType(5))
        self.assertEquals(IDiskDriveConstants.TYPE_COMPACT_DISK, self.drive.getDriveType())
        self.assertEquals(IDiskDriveConstants.TYPE_RAM_DISK, self.drive.setDriveType(6))
        self.assertEquals(IDiskDriveConstants.TYPE_RAM_DISK, self.drive.getDriveType())
        
        self.assertRaises(IllegalArgumentError, self.drive.setDriveType, 7)
        self.assertRaises(IllegalArgumentError, self.drive.setDriveType, -1)
        
        self.assertRaises(IllegalArgumentError, self.drive.setDriveType, "1")
        self.assertRaises(TypeError, self.drive.setDriveType, True)
        self.assertRaises(TypeError, self.drive.setDriveType, False)
        self.assertRaises(TypeError, self.drive.setDriveType, 0.15)
    
    def test_set_get_file_system(self):
        self.assertEquals("nt", self.drive.setFileSystem("nt"))
        self.assertEquals("nt", self.drive.getFileSystem())
        
        self.assertRaises(TypeError, self.drive.setFileSystem, 1)
        self.assertRaises(TypeError, self.drive.setFileSystem, True)
        self.assertRaises(TypeError, self.drive.setFileSystem, False)
        self.assertRaises(TypeError, self.drive.setFileSystem, 0.56)
        
        
    def test_set_get_free_space(self):
        self.assertEquals(1024, self.drive.setFreeSpace(1024))
        self.assertEquals(1024, self.drive.getFreeSpace())
    
        self.assertRaises(IllegalArgumentError, self.drive.setFreeSpace, -1)
    
        self.assertRaises(TypeError, self.drive.setFreeSpace, "1")
        self.assertRaises(TypeError, self.drive.setFreeSpace, True)
        self.assertRaises(TypeError, self.drive.setFreeSpace, False)
        self.assertRaises(TypeError, self.drive.setFreeSpace, 0.15)
    
    def test_set_get_size(self):
        self.assertEquals(1024, self.drive.setSize(1024))
        self.assertEquals(1024, self.drive.getSize())
        
        self.assertRaises(IllegalArgumentError, self.drive.setSize, -1)
        
        self.assertRaises(TypeError, self.drive.setSize, "1")
        self.assertRaises(TypeError, self.drive.setSize, True)
        self.assertRaises(TypeError, self.drive.setSize, False)
        self.assertRaises(TypeError, self.drive.setSize, 0.15)
        
    def test_set_get_volume_name(self):
        self.assertEquals("C", self.drive.setVolumeName("C"))
        self.assertEquals("C", self.drive.getVolumeName())
        
        self.assertRaises(TypeError, self.drive.setVolumeName, 1)
        self.assertRaises(TypeError, self.drive.setVolumeName, True)
        self.assertRaises(TypeError, self.drive.setVolumeName, False)
        self.assertRaises(TypeError, self.drive.setVolumeName, 0.56)