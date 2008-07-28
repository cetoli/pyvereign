from org.pyvereign.base.interface import implements
from org.pyvereign.environment.instrumentation.dataaccess.ibattery_dao import IBatteryDAO
from org.pyvereign.environment.instrumentation.dataaccess.windows.windows_battery_dao import WindowsBatteryDAO
from org.pyvereign.environment.instrumentation.hardware.ibattery import IBattery
import unittest

class WindowsBatteryDAOTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(WindowsBatteryDAO())
        self.assertTrue(implements(WindowsBatteryDAO(), IBatteryDAO))
        
    def test_retrieve_battery(self):
        dao = WindowsBatteryDAO()
        self.assertTrue(dao.retrieveBattery())
        self.assertTrue(implements(dao.retrieveBattery(), IBattery))
        
        battery = dao.retrieveBattery()
        self.assertTrue(battery.getEstimatedChargeRemaining() >= 0 and battery.getEstimatedChargeRemaining() <= 100)
        self.assertTrue(battery.getDescription() <> None)
        self.assertTrue(battery.getEstimatedChargeRemaining() <> None)
        self.assertTrue(battery.getHardwareId() <> None)
        self.assertTrue(battery.getLogicalName()  <> None)
        self.assertTrue(battery.getProduct()  <> None)
        self.assertTrue(battery.getSerial()  <> None)