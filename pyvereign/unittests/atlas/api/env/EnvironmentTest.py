from atlas.api.env.Environment import Environment
from atlas.api.env.transport.address.IPv4Address import IPv4Address
import unittest

environment = Environment()
environment.initialize()
environment.start()

class EnvironmentTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(Environment())
    
    def test_environment_machine_getlogicalname(self):
        self.assertEquals("COVERDALE", environment.executeService("machine", "getLogicalName"))
    
    def test_environment_machine_getdomain(self):
        self.assertEquals("GRUPO", environment.executeService("machine", "getDomain"))
    
    def test_environment_machine_getdescription(self):
        self.assertEquals("AT/AT COMPATIBLE", environment.executeService("machine", "getDescription"))
    
    def test_environment_machine_getproduct(self):
        self.assertEquals("HP Pavilion dv9000 (RP115UA#ABA)  ", environment.executeService("machine", "getProduct"))
        
    def test_environment_machine_getVendor(self):
        self.assertEquals("Hewlett-Packard", environment.executeService("machine", "getVendor"))
        
    def test_environment_machine_getserial(self):
        self.assertEquals("HP Pavilion dv9000 (RP115UA#ABA)  ", environment.executeService("machine", "getSerial"))
        
    def test_environment_machine_gethardwareid(self):
        self.assertEquals("COVERDALE", environment.executeService("machine", "getHardwareId"))
        
    def test_environment_machine_getnumberprocessors(self):
        self.assertEquals(2, environment.executeService("machine", "getNumberOfProcessors"))
    
    def test_environment_machine_gettotalphysicalmemory(self):
        self.assertEquals(2078838784, environment.executeService("machine", "getTotalPhysicalMemory"))
    
    def test_environment_machine_getname(self):
        self.assertEquals("machine", environment.executeService("machine", "getName"))
    
    def test_environment_network_controller_getnetworkcontrollers(self):
        self.assertTrue(len(environment.executeService("network_controller", "getNetworkControllers")) > 0)
    
    def test_environment_network_controller_getMACAddresses(self):
        self.assertTrue(len(environment.executeService("network_controller", "getMACAddresses")) > 0)
    
    def test_environment_network_controller_getIPAddresses(self):
        self.assertTrue(len(environment.executeService("network_controller", "getIPAddresses")) > 0)
    
    def test_environment_protocol_getprotocols(self):
        self.assertTrue(len(environment.executeService("protocol", "getProtocols")) > 0)
        
    def test_send_stream_by_using_stream_fowarder(self):
        self.assertEquals("environment", environment.executeService("transport", "sendStream", "TCP", IPv4Address("127.0.0.1", 5050), "environment"))