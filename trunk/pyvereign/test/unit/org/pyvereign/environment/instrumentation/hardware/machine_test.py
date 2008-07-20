from org.pyvereign.environment.instrumentation.hardware.machine import Machine
from org.pyvereign.base.interface import implements
from org.pyvereign.environment.instrumentation.hardware.ihardware import IHardware
from org.pyvereign.environment.instrumentation.hardware.imachine import IMachine
from org.pyvereign.error.illegal_argument_error import IllegalArgumentError
import unittest

class MachineTest(unittest.TestCase):
    
    def setUp(self):
        self.machine = Machine()
    
    def test_create_instance(self):
        self.assertTrue(Machine())
        machine = Machine()
        self.assertEquals("", machine.getDomain())
        self.assertEquals(1, machine.getNumberOfProcessors())
        self.assertEquals(0, machine.getTotalPhysicalMemory())
        
        self.assertTrue(implements(machine, IHardware, IMachine))
    
    def test_set_get_domain(self):
        self.assertEquals("teste", self.machine.setDomain("teste"))
        self.assertEquals("teste", self.machine.getDomain())
        
        self.assertRaises(TypeError, self.machine.setDomain, 1)
        self.assertRaises(TypeError, self.machine.setDomain, True)
        self.assertRaises(TypeError, self.machine.setDomain, False)
        self.assertRaises(TypeError, self.machine.setDomain, 0.665)
    
    def test_set_get_number_of_processors(self):
        self.assertEquals(1, self.machine.setNumberOfProcessors(1))
        self.assertEquals(1, self.machine.getNumberOfProcessors())
        self.assertEquals(4, self.machine.setNumberOfProcessors(4))
        self.assertEquals(4, self.machine.getNumberOfProcessors())
        
        self.assertRaises(IllegalArgumentError, self.machine.setNumberOfProcessors, 0)
        self.assertRaises(IllegalArgumentError, self.machine.setNumberOfProcessors, -1)
        
        self.assertRaises(TypeError, self.machine.setNumberOfProcessors, "2")
        self.assertRaises(TypeError, self.machine.setNumberOfProcessors, True)
        self.assertRaises(IllegalArgumentError, self.machine.setNumberOfProcessors, False)
        self.assertRaises(IllegalArgumentError, self.machine.setNumberOfProcessors, 0.665)
    
    def test_set_get_total_physical_memory(self):
        self.assertEquals(1024, self.machine.setTotalPhysicalMemory(1024))
        self.assertEquals(1024, self.machine.getTotalPhysicalMemory())
        
        self.assertRaises(IllegalArgumentError, self.machine.setTotalPhysicalMemory, -1)
        
        self.assertRaises(TypeError, self.machine.setTotalPhysicalMemory, "2")
        self.assertRaises(TypeError, self.machine.setTotalPhysicalMemory, True)
        self.assertRaises(TypeError, self.machine.setTotalPhysicalMemory, False)
        self.assertRaises(TypeError, self.machine.setTotalPhysicalMemory, 0.665)
    
        