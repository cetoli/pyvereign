from org.pyvereign.core.environment.instrumentation.dao.hardware.windows.WindowsBatteryDAO import WindowsBatteryDAO
import unittest

class WindowsBatteryDAOTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(WindowsBatteryDAO())
        
    def test_retrieve_battery(self):
        dao = WindowsBatteryDAO()
        self.assertTrue(dao.retrieveBattery())
        battery = dao.retrieveBattery()
        
        self.assertTrue(battery.getDescription())
        self.assertTrue(battery.getEstimatedChargeRemaining())
        self.assertTrue(battery.getHardwareId())
        self.assertTrue(battery.getLogicalName())
        self.assertTrue(battery.getProduct())
        self.assertTrue(battery.getSerial())
        self.assertFalse(battery.getVendor())