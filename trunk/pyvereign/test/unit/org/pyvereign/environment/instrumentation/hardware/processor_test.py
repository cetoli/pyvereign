from org.pyvereign.environment.instrumentation.hardware.processor import Processor
from org.pyvereign.base.interface import implements
from org.pyvereign.environment.instrumentation.hardware.ihardware import IHardware
from org.pyvereign.environment.instrumentation.hardware.iprocessor import IProcessor
from org.pyvereign.error.illegal_argument_error import IllegalArgumentError
import unittest

class ProcessorTest(unittest.TestCase):
    
    def setUp(self):
        self.processor = Processor()
    
    def test_create_instance(self):
        self.assertTrue(Processor())
        processor = Processor()
        self.assertEquals(Processor.ARCH_X86, processor.getArchitecture())
        self.assertEquals(Processor.ST_UNKNOW, processor.getCPUStatus())
        self.assertEquals(0, processor.getCurrentClockSpeed())
        self.assertEquals(0, processor.getL2CacheSize())
        self.assertEquals(0, processor.getL2CacheSpeed())
        self.assertEquals(0, processor.getLoadPercentage())
        self.assertEquals(0, processor.getMaxClockSpeed())
        self.assertEquals("", processor.getProcessorId())
        self.assertEquals(Processor.PROC_TYPE_OTHER, processor.getProcessorType())
        self.assertTrue(implements(processor, IHardware, IProcessor))
        
    def test_set_get_architecture(self):
        self.assertEquals(Processor.ARCH_X86, self.processor.setArchitecture(0))
        self.assertEquals(Processor.ARCH_X86, self.processor.getArchitecture())
        self.assertEquals(Processor.ARCH_MIPS, self.processor.setArchitecture(1))
        self.assertEquals(Processor.ARCH_MIPS, self.processor.getArchitecture())
        self.assertEquals(Processor.ARCH_ALPHA, self.processor.setArchitecture(2))
        self.assertEquals(Processor.ARCH_ALPHA, self.processor.getArchitecture())
        self.assertEquals(Processor.ARCH_POWER_PC, self.processor.setArchitecture(3))
        self.assertEquals(Processor.ARCH_POWER_PC, self.processor.getArchitecture())
        self.assertEquals(Processor.ARCH_IPF, self.processor.setArchitecture(6))
        self.assertEquals(Processor.ARCH_IPF, self.processor.getArchitecture())
        self.assertEquals(Processor.ARCH_X64, self.processor.setArchitecture(9))
        self.assertEquals(Processor.ARCH_X64, self.processor.getArchitecture())
        
        self.assertRaises(IllegalArgumentError, self.processor.setArchitecture, -1)
        self.assertRaises(IllegalArgumentError, self.processor.setArchitecture, 10)
        
        self.assertRaises(IllegalArgumentError, self.processor.setArchitecture, "a")
        self.assertRaises(TypeError, self.processor.setArchitecture, True)
        self.assertRaises(TypeError, self.processor.setArchitecture, False)
        self.assertRaises(TypeError, self.processor.setArchitecture, 0.99)
        