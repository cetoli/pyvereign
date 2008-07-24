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
        
    def test_set_get_current_clock_speed(self):
        self.assertEquals(1600, self.processor.setCurrentClockSpeed(1600))
        self.assertEquals(1600, self.processor.getCurrentClockSpeed())
        
        self.assertRaises(IllegalArgumentError, self.processor.setCurrentClockSpeed, -1)
        
        self.assertRaises(TypeError, self.processor.setCurrentClockSpeed, "2000")
        self.assertRaises(TypeError, self.processor.setCurrentClockSpeed, True)
        self.assertRaises(TypeError, self.processor.setCurrentClockSpeed, False)
        self.assertRaises(TypeError, self.processor.setCurrentClockSpeed, 0.555)
    
    def test_set_get_l2_cache_size(self):
        self.assertEquals(512, self.processor.setL2CacheSize(512))
        self.assertEquals(512, self.processor.getL2CacheSize())
        
        self.assertRaises(IllegalArgumentError, self.processor.setCurrentClockSpeed, -1)
        
        self.assertRaises(TypeError, self.processor.setL2CacheSize, "1024")
        self.assertRaises(TypeError, self.processor.setL2CacheSize, True)
        self.assertRaises(TypeError, self.processor.setL2CacheSize, False)
        self.assertRaises(TypeError, self.processor.setL2CacheSize, 0.555)
    
    def test_set_get_l2_cache_speed(self):
        self.assertEquals(200, self.processor.setL2CacheSpeed(200))
        self.assertEquals(200, self.processor.getL2CacheSpeed())
        
        self.assertRaises(IllegalArgumentError, self.processor.setL2CacheSpeed, -1)
        
        self.assertRaises(TypeError, self.processor.setL2CacheSpeed, "1024")
        self.assertRaises(TypeError, self.processor.setL2CacheSpeed, True)
        self.assertRaises(TypeError, self.processor.setL2CacheSpeed, False)
        self.assertRaises(TypeError, self.processor.setL2CacheSpeed, 0.555)
    
    def test_set_get_load_percentage(self):
        self.assertEquals(50, self.processor.setLoadPercentage(50))
        self.assertEquals(50, self.processor.getLoadPercentage())
        
        self.assertRaises(IllegalArgumentError, self.processor.setLoadPercentage, -1)
        self.assertRaises(IllegalArgumentError, self.processor.setLoadPercentage, 101)
        
        self.assertRaises(IllegalArgumentError, self.processor.setLoadPercentage, "1024")
        self.assertRaises(TypeError, self.processor.setLoadPercentage, True)
        self.assertRaises(TypeError, self.processor.setLoadPercentage, False)
        self.assertRaises(TypeError, self.processor.setLoadPercentage, 0.555)
        
    def test_set_get_max_clock_speed(self):
        self.assertEquals(1600, self.processor.setMaxClockSpeed(1600))
        self.assertEquals(1600, self.processor.getMaxClockSpeed())
        
        self.assertRaises(IllegalArgumentError, self.processor.setMaxClockSpeed, -1)
        
        self.assertRaises(TypeError, self.processor.setMaxClockSpeed, "1024")
        self.assertRaises(TypeError, self.processor.setMaxClockSpeed, True)
        self.assertRaises(TypeError, self.processor.setMaxClockSpeed, False)
        self.assertRaises(TypeError, self.processor.setMaxClockSpeed, 0.555)
    
    def test_set_get_processor_id(self):
        self.assertEquals("123456", self.processor.setProcessorId("123456"))
        self.assertEquals("123456", self.processor.getProcessorId())
        
        self.assertRaises(TypeError, self.processor.setProcessorId, 1024)
        self.assertRaises(TypeError, self.processor.setProcessorId, True)
        self.assertRaises(TypeError, self.processor.setProcessorId, False)
        self.assertRaises(TypeError, self.processor.setProcessorId, 0.555)
        
    def test_set_get_processor_type(self):
        self.assertEquals(Processor.PROC_TYPE_OTHER, self.processor.setProcessorType(1))
        self.assertEquals(Processor.PROC_TYPE_OTHER, self.processor.getProcessorType())
        self.assertEquals(Processor.PROC_TYPE_UNKNOW, self.processor.setProcessorType(2))
        self.assertEquals(Processor.PROC_TYPE_UNKNOW, self.processor.getProcessorType())
        self.assertEquals(Processor.PROC_TYPE_CENTRAL_PROCESSOR, self.processor.setProcessorType(3))
        self.assertEquals(Processor.PROC_TYPE_CENTRAL_PROCESSOR, self.processor.getProcessorType())
        self.assertEquals(Processor.PROC_TYPE_MATH_PROCESSOR, self.processor.setProcessorType(4))
        self.assertEquals(Processor.PROC_TYPE_MATH_PROCESSOR, self.processor.getProcessorType())
        self.assertEquals(Processor.PROC_TYPE_DSP_PROCESSOR, self.processor.setProcessorType(5))
        self.assertEquals(Processor.PROC_TYPE_DSP_PROCESSOR, self.processor.getProcessorType())
        self.assertEquals(Processor.PROC_TYPE_VIDEO_PROCESSOR, self.processor.setProcessorType(6))
        self.assertEquals(Processor.PROC_TYPE_VIDEO_PROCESSOR, self.processor.getProcessorType())
        
        self.assertRaises(IllegalArgumentError, self.processor.setProcessorType, -1)
        self.assertRaises(IllegalArgumentError, self.processor.setProcessorType, 0)
        self.assertRaises(IllegalArgumentError, self.processor.setProcessorType, 7)
        
        self.assertRaises(IllegalArgumentError, self.processor.setProcessorType, "1024")
        self.assertRaises(TypeError, self.processor.setProcessorType, True)
        self.assertRaises(IllegalArgumentError, self.processor.setProcessorType, False)
        self.assertRaises(IllegalArgumentError, self.processor.setProcessorType, 0.555)