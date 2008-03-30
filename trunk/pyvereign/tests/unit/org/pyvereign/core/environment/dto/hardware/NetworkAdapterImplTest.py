from org.pyvereign.core.environment.dto.hardware.NetworkAdapterImpl import NetworkAdapterImpl
import unittest

class NetworkAdapterImplTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(NetworkAdapterImpl({}))
        
        values = {"description": "adapter", "product": "adapter", "hardwareId": "abc",
                  "serial": "1234", "vendor": "fabricante", "logicalName": "adapter",
                  "speed": 100000, "macAddress": "AA", "ipAddress": "192.168.0.12"}
        
        adapter = NetworkAdapterImpl(values)
        self.assertEquals("adapter", adapter.getDescription())
        self.assertEquals("adapter", adapter.getProduct())
        self.assertEquals("abc", adapter.getHardwareId())
        self.assertEquals("1234", adapter.getSerial())
        self.assertEquals("fabricante", adapter.getVendor())
        self.assertEquals("adapter", adapter.getLogicalName())
        self.assertEquals(100000, adapter.getSpeed())
        self.assertEquals("AA", adapter.getMACAddress())
        self.assertEquals("192.168.0.12", adapter.getIPAddress())