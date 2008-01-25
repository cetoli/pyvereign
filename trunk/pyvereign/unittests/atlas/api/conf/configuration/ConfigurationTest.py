from atlas.api.conf.property.DefaultProperty import DefaultProperty
from atlas.api.conf.property.CompositeProperty import CompositeProperty
from atlas.api.conf.configuration.Configuration import Configuration
import unittest

class ConfigurationTest(unittest.TestCase):
    
    def test_save_simple_configuration(self):
        memory = DefaultProperty("memory", 1024)
        disk = DefaultProperty("disk", 2048)
        network = DefaultProperty("network", 100)
        conf = Configuration()
        self.assertEquals(memory, conf.addProperty(memory))
        self.assertEquals(disk, conf.addProperty(disk))
        self.assertEquals(network, conf.addProperty(network))
        self.assertEquals(3, conf.getNumberOfProperties()) 
        conf.save("test1.yaml")
        conf.clear()
        self.assertEqual(0, conf.getNumberOfProperties())
        conf.load("test1.yaml")
        self.assertTrue(conf.hasProperty("memory"))
        self.assertTrue(conf.hasProperty("disk"))
        self.assertTrue(conf.hasProperty("network"))
    
    def test_save_composite_configuration(self):
        property = CompositeProperty("windows")
        device = CompositeProperty("device")
        memory = DefaultProperty("memory", 1024)
        disk = DefaultProperty("disk", 2048)
        self.assertEquals(memory, device.addProperty(memory))
        self.assertEquals(disk, device.addProperty(disk))
        self.assertEquals(device, property.addProperty(device))
        property.setLevel(1)
        self.assertEquals(1, property.getLevel())
        self.assertEquals(2, device.getLevel())
        self.assertEquals(3, memory.getLevel())
        self.assertEquals(3, disk.getLevel())
        self.assertEquals(1, property.getNumberOfProperties())
        
        conf = Configuration()
        self.assertEquals(property, conf.addProperty(property))
        
        conf.save("test2.yaml")
        conf.clear()
        conf.load("test2.yaml")
        
        self.assertTrue(conf.hasProperty("windows"))
        windows = conf.getProperty("windows")
        self.assertTrue(windows.hasProperty("device"))
        device = windows.getProperty("device")
        self.assertTrue(device.hasProperty("memory"))
        self.assertTrue(device.hasProperty("disk"))
        memory = device.getProperty("memory")
        disk = device.getProperty("disk")
        self.assertEquals(1024, memory.getValue())
        self.assertEquals(2048, disk.getValue())
    
    def test_load_simple_configuration(self):
        conf = Configuration()
        conf.load("teste.yaml")
        self.assertEquals(2, conf.getNumberOfProperties())
        self.assertTrue(conf.getProperties())
        self.assertEquals(2, len(conf.getProperties()))
        self.assertTrue(conf.hasProperty("windows"))
        
        windows = conf.getProperty("windows")
        self.assertEquals("windows", windows.getName())
        self.assertTrue(windows.hasProperty("module"))
        self.assertTrue(windows.isComposite())
        self.assertEquals(3, windows.getNumberOfProperties())
        
        module = windows.getProperty("module")
        self.assertFalse(module.isComposite())
        self.assertEquals("module", module.getName())
        self.assertEquals("atlas.api.environment.windows", module.getValue())
        
        self.assertTrue(windows.hasProperty("classname"))
        classname = windows.getProperty("classname")
        self.assertFalse(module.isComposite())
        self.assertEquals("classname", classname.getName())
        self.assertEquals("Windows", classname.getValue())
        
        self.assertTrue(windows.hasProperty("host"))
        host = windows.getProperty("host")
        self.assertTrue(host.isComposite())
        self.assertEquals(2, host.getNumberOfProperties())
        
        self.assertTrue(host.hasProperty("name"))
        name = host.getProperty("name")
        self.assertEquals("coverdale", name.getValue())
        self.assertEquals("name", name.getName())
        
        self.assertTrue(host.hasProperty("ip"))
        ip = host.getProperty("ip")
        self.assertEquals("ip", ip.getName())
        self.assertEquals("192.168.1.2", ip.getValue())
        
        self.assertTrue(conf.hasProperty("linux"))
        linux = conf.getProperty("linux")
        self.assertTrue(linux.hasProperty("module"))
        self.assertTrue(linux.isComposite())
        self.assertEquals(4, linux.getNumberOfProperties())
        
        module = linux.getProperty("module")
        self.assertFalse(module.isComposite())
        self.assertEquals("module", module.getName())
        self.assertEquals("atlas.api.environment.linux", module.getValue())
        
        self.assertTrue(linux.hasProperty("classname"))
        classname = linux.getProperty("classname")
        self.assertFalse(module.isComposite())
        self.assertEquals("classname", classname.getName())
        self.assertEquals("Linux", classname.getValue())
        
        self.assertTrue(linux.hasProperty("host"))
        host = linux.getProperty("host")
        self.assertTrue(host.isComposite())
        self.assertEquals(2, host.getNumberOfProperties())
        
        self.assertTrue(host.hasProperty("name"))
        name = host.getProperty("name")
        self.assertEquals("coverdale", name.getValue())
        self.assertEquals("name", name.getName())
        
        self.assertTrue(host.hasProperty("ip"))
        ip = host.getProperty("ip")
        self.assertEquals("ip", ip.getName())
        self.assertEquals("192.168.1.2", ip.getValue())
        
        self.assertTrue(linux.hasProperty("distribution"))
        dist = linux.getProperty("distribution")
        self.assertEquals("distribution", dist.getName())
        self.assertEquals(3, dist.getNumberOfProperties())
        self.assertTrue(dist.isComposite())
        
        self.assertTrue(dist.hasProperty("name"))
        name = dist.getProperty("name")
        self.assertEquals("name", name.getName())
        self.assertEquals("Ubuntu", name.getValue())
        
        self.assertTrue(dist.hasProperty("version"))
        version = dist.getProperty("version")
        self.assertEquals("version", version.getName())
        self.assertEquals("7.10", str(version.getValue()))
        
        self.assertTrue(dist.hasProperty("platform"))
        platform = dist.getProperty("platform")
        self.assertTrue(platform.isComposite())
        self.assertEquals("platform", platform.getName())
        self.assertEquals(2, platform.getNumberOfProperties())
        
        self.assertTrue(platform.hasProperty("type"))
        type = platform.getProperty("type")
        self.assertEquals("32 bits", type.getValue())
        self.assertEquals("type", type.getName())
        
        self.assertTrue(platform.hasProperty("name"))
        name = platform.getProperty("name")
        self.assertEquals("x86", name.getValue())
        self.assertEquals("name", name.getName())
#    "linux": 
#  {
#    "module": "atlas.api.environment.linux"
#  classname: Linux
#  host:
#    name: coverdale
#    ip: 192.168.1.2
#  distribution:
#    name: Ubuntu
#    version: 7.10
#    platform:
#      type: 32 bits
#      name: x86
        
    
    def test_try_save_configuration_on_non_existent_path(self):
        conf = Configuration()
        conf.addProperty(DefaultProperty("class", "Class"))
        self.assertRaises(IOError, conf.save, "/raise/raise.yaml")
    
    def test_try_load_non_existent_configuration(self):
        conf = Configuration()
        self.assertRaises(IOError, conf.load, "raise.yaml")