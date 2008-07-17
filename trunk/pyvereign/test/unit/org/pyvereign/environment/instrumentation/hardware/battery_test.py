from org.pyvereign.environment.instrumentation.hardware.battery import Battery
from org.pyvereign.base.interface import implements
from org.pyvereign.environment.instrumentation.hardware.ihardware import IHardware
from org.pyvereign.environment.instrumentation.hardware.ibattery import IBattery
from org.pyvereign.error.IllegalArgumentError import IllegalArgumentError
import unittest

class BatteryTest(unittest.TestCase):
    
    def setUp(self):
        self.battery = Battery()
    
    def test_try_create_intance(self):
        self.assertTrue(Battery())
        battery = Battery()
        self.assertEquals("", battery.getDescription())
        self.assertEquals("", battery.getHardwareId())
        self.assertEquals("", battery.getLogicalName())
        self.assertEquals("", battery.getProduct())
        self.assertEquals("", battery.getSerial())
        self.assertEquals("", battery.getVendor())
        self.assertEquals(0, battery.getEstimatedChargeRemaining())
        
        self.assertTrue(implements(battery, IHardware, IBattery))
    
    def test_set_get_EstimatedChargeRemaining(self):
        self.assertEquals(10, self.battery.setEstimatedChargeRemaining(10))
        self.assertEquals(0, self.battery.setEstimatedChargeRemaining(0))
        self.assertEquals(100, self.battery.setEstimatedChargeRemaining(100))
        
        self.assertRaises(IllegalArgumentError, self.battery.setEstimatedChargeRemaining, -1)
        self.assertRaises(IllegalArgumentError, self.battery.setEstimatedChargeRemaining, 110)
        
        self.assertRaises(IllegalArgumentError, self.battery.setEstimatedChargeRemaining, "1")
        self.assertRaises(TypeError, self.battery.setEstimatedChargeRemaining, False)
        self.assertRaises(TypeError, self.battery.setEstimatedChargeRemaining, True)
        self.assertRaises(TypeError, self.battery.setEstimatedChargeRemaining, 0.001)
        