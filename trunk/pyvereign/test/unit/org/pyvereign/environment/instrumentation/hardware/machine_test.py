from org.pyvereign.environment.instrumentation.hardware.machine import Machine
from org.pyvereign.base.interface import implements
from org.pyvereign.environment.instrumentation.hardware.ihardware import IHardware
from org.pyvereign.environment.instrumentation.hardware.imachine import IMachine
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