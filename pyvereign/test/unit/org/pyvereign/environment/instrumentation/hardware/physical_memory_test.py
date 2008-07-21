from org.pyvereign.environment.instrumentation.hardware.physical_memory import PhysicalMemory
from org.pyvereign.base.interface import implements
from org.pyvereign.environment.instrumentation.hardware.ihardware import IHardware
from org.pyvereign.environment.instrumentation.hardware.iphysical_memory import IPhysicalMemory
import unittest

class PhysicalMemoryTest(unittest.TestCase):
    
    def setUp(self):
        self.memory = PhysicalMemory()
    
    def test_try_create_test(self):
        self.assertTrue(PhysicalMemory())
        memory = PhysicalMemory()
        self.assertEquals(0, memory.getCapacity())
        self.assertEquals(0, memory.getDataWidth())
        self.assertEquals(0, memory.getSpeed())
        
        self.assertTrue(implements(memory, IHardware, IPhysicalMemory))
        
    def test_set_get_capacity(self):
        self.assertEquals(1024, self.memory.setCapacity(1024))
        self.assertEquals(1024, self.memory.getCapacity())
        
        self.assertRaises(TypeError, self.memory.setCapacity, "1024")
        self.assertRaises(TypeError, self.memory.setCapacity, True)
        self.assertRaises(TypeError, self.memory.setCapacity, False)
        self.assertRaises(TypeError, self.memory.setCapacity, 0.65)
    
    def test_set_get_data_width(self):
        self.assertEquals(1024, self.memory.setDataWidth(1024))
        self.assertEquals(1024, self.memory.getDataWidth())
        
        self.assertRaises(TypeError, self.memory.setDataWidth, "1024")
        self.assertRaises(TypeError, self.memory.setDataWidth, True)
        self.assertRaises(TypeError, self.memory.setDataWidth, False)
        self.assertRaises(TypeError, self.memory.setDataWidth, 0.65)
    
    def test_set_get_speed(self):
        self.assertEquals(1024, self.memory.setSpeed(1024))
        self.assertEquals(1024, self.memory.getSpeed())
        
        self.assertRaises(TypeError, self.memory.setSpeed, "1024")
        self.assertRaises(TypeError, self.memory.setSpeed, True)
        self.assertRaises(TypeError, self.memory.setSpeed, False)
        self.assertRaises(TypeError, self.memory.setSpeed, 0.65)