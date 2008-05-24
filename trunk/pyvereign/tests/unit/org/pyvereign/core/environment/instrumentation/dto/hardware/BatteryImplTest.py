from org.pyvereign.core.environment.instrumentation.dto.hardware.BatteryImpl import BatteryImpl
import unittest

class BatteryImplTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(BatteryImpl({}))
        
        values = {"description": "Battery", "estimatedChargeRemaining": 50, 
                  "hardwareId": "123", "logicalName": "Battery", "product": "Battery",
                  "serial": "123a", "vendor": "CE"}
        
        battery = BatteryImpl(values)
        
        self.assertEquals("Battery", battery.getDescription())
        self.assertEquals(50, battery.getEstimatedChargeRemaining())
        self.assertEquals("123", battery.getHardwareId())
        self.assertEquals("Battery", battery.getLogicalName())
        self.assertEquals("Battery", battery.getProduct())
        self.assertEquals("123a", battery.getSerial())
        self.assertEquals("CE", battery.getVendor())
        
    def test_try_create_instance(self):
        self.assertRaises(RuntimeError, BatteryImpl, {"test": 123})