from org.pyvereign.core.environment.instrumentation.dao.hardware.windows.WindowsBatteryDAO import WindowsBatteryDAO
import unittest

class WindowsBatteryDAOTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(WindowsBatteryDAO())
        
    def test_retrieve_battery(self):
        dao = WindowsBatteryDAO()
        self.assertTrue(dao.retrieveBattery())
        battery = dao.retrieveBattery()
        
        self.assertTrue(battery.getDescription() <> None)
        self.assertTrue(battery.getEstimatedChargeRemaining() <> None)
        self.assertTrue(battery.getHardwareId() <> None)
        self.assertTrue(battery.getLogicalName()  <> None)
        self.assertTrue(battery.getProduct()  <> None)
        self.assertTrue(battery.getSerial()  <> None)
