from atlas.api.env.Environment import Environment
import unittest

class EnvironmentTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(Environment())
    
    def test_environment_machine_getlogicalname(self):
        environment = Environment()
        environment.initialize()
        environment.start()
        
        self.assertEquals("COVERDALE", environment.executeService("machine", "getLogicalName"))
    
    def test_environment_machine_getdomain(self):
        environment = Environment()
        environment.initialize()
        environment.start()
        
        self.assertEquals("GRUPO", environment.executeService("machine", "getDomain"))
    
    def test_environment_machine_getdescription(self):
        environment = Environment()
        environment.initialize()
        environment.start()
        
        self.assertEquals("AT/AT COMPATIBLE", environment.executeService("machine", "getDescription"))
    
    def test_environment_machine_getproduct(self):
        environment = Environment()
        environment.initialize()
        environment.start()
        
        self.assertEquals("HP Pavilion dv9000 (RP115UA#ABA)  ", environment.executeService("machine", "getProduct"))
        
    def test_environment_machine_getVendor(self):
        environment = Environment()
        environment.initialize()
        environment.start()
        
        self.assertEquals("Hewlett-Packard", environment.executeService("machine", "getVendor"))
        
    def test_environment_machine_getserial(self):
        environment = Environment()
        environment.initialize()
        environment.start()
        
        self.assertEquals("HP Pavilion dv9000 (RP115UA#ABA)  ", environment.executeService("machine", "getSerial"))
        
    def test_environment_machine_gethardwareid(self):
        environment = Environment()
        environment.initialize()
        environment.start()
        
        self.assertEquals("COVERDALE", environment.executeService("machine", "getHardwareId"))
        
    def test_environment_machine_getnumberprocessors(self):
        environment = Environment()
        environment.initialize()
        environment.start()
        
        self.assertEquals(2, environment.executeService("machine", "getNumberOfProcessors"))
    
    def test_environment_machine_gettotalphysicalmemory(self):
        environment = Environment()
        environment.initialize()
        environment.start()
        
        self.assertEquals(2078838784, environment.executeService("machine", "getTotalPhysicalMemory"))
    
    def test_environment_machine_getname(self):
        environment = Environment()
        environment.initialize()
        environment.start()
        
        self.assertEquals("machine", environment.executeService("machine", "getName"))
    
    def test_environment_network_controller_getnetworkcontrollers(self):
        environment = Environment()
        environment.initialize()
        environment.start()
        
        self.assertTrue(len(environment.executeService("network_controller", "getNetworkControllers")) > 0)
    
    def test_environment_network_controller_getMACAddresses(self):
        environment = Environment()
        environment.initialize()
        environment.start()
        
        self.assertTrue(len(environment.executeService("network_controller", "getMACAddresses")) > 0)
    
    def test_environment_network_controller_getIPAddresses(self):
        environment = Environment()
        environment.initialize()
        environment.start()
        
        self.assertTrue(len(environment.executeService("network_controller", "getIPAddresses")) > 0)
    
    def test_environment_protocol_getprotocols(self):
        environment = Environment()
        environment.initialize()
        environment.start()
        
        self.assertTrue(len(environment.executeService("protocol", "getProtocols")) > 0)