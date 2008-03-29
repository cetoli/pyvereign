from org.pyvereign.core.environment.dao.hardware.windows.WindowsDiskDriveDAO import WindowsDiskDriveDAO
import unittest

class WindowsDiskDriveDAOTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(WindowsDiskDriveDAO())
        
    def test_retrieve_diskdrives(self):
        dao = WindowsDiskDriveDAO()
        diskdrives = dao.retrieveDiskDrives()
        self.assertTrue(diskdrives)
        self.assertTrue(len(diskdrives) >= 1)