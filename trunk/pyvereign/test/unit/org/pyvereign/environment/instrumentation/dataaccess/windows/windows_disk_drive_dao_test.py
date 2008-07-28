from org.pyvereign.environment.instrumentation.dataaccess.windows.windows_disk_drive_dao import WindowsDiskDriveDAO
from org.pyvereign.base.interface import implements
from org.pyvereign.environment.instrumentation.dataaccess.idisk_drive_dao import IDiskDriveDAO
from org.pyvereign.environment.instrumentation.hardware.idisk_drive import IDiskDrive
import unittest

class WindowsDiskDriveDAOTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(WindowsDiskDriveDAO())
        self.assertTrue(implements(WindowsDiskDriveDAO(), IDiskDriveDAO))
        
    def test_retrieve_dis_drives(self):
        dao = WindowsDiskDriveDAO()
        self.assertTrue(dao.retrieveDiskDrives())
        self.assertTrue(len(dao.retrieveDiskDrives()) > 0)
        
        diskdrives = dao.retrieveDiskDrives()
        
        for drive in diskdrives:
            self.assertTrue(implements(drive, IDiskDrive))
            self.assertTrue(drive.getDescription())
            self.assertTrue(drive.getDriveType())
            self.assertTrue(drive.getFileSystem())
            self.assertTrue(drive.getFreeSpace())
            self.assertTrue(drive.getHardwareId())
            self.assertTrue(drive.getLogicalName())
            self.assertTrue(drive.getProduct())
            self.assertTrue(drive.getSerial())
            self.assertTrue(drive.getSize())
        