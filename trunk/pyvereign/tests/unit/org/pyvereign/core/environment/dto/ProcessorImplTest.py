from org.pyvereign.core.environment.dto.hardware.ProcessorImpl import ProcessorImpl
import unittest

class ProcessorImplTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(ProcessorImpl())
        
        values = {"architecture": 0, "cpuStatus": 1, "currentClockSpeed": 1607, 
                  "description": "Turion", "hardwareId": "123", "l2CacheSize": 512,
                  "l2CacheSpeed": 0, "loadPercentage": 7, "logicalName": "CPU0",
                  "maxClockSpeed": 1607, "processorId": "145", "processorType": 3,
                  "product": "AMD Processor", "serial": "abc123", "vendor": "AMD"}
        processor = ProcessorImpl(values)
        self.assertEquals(ProcessorImpl.ARCH_X86, processor.getArchitecture())
        self.assertEquals(ProcessorImpl.ST_CPU_ENABLE, processor.getCPUStatus())
        self.assertEquals(1607, processor.getCurrentClockSpeed())
        self.assertEquals("Turion", processor.getDescription())
        self.assertEquals("123", processor.getHardwareId())
        self.assertEquals(512, processor.getL2CacheSize())
        self.assertEquals(0, processor.getL2CacheSpeed())
        self.assertEquals(7, processor.getLoadPercentage())
        self.assertEquals("CPU0", processor.getLogicalName())
        self.assertEquals(1607, processor.getMaxClockSpeed())
        self.assertEquals("145", processor.getProcessorId())
        self.assertEquals(ProcessorImpl.PROC_TYPE_CENTRAL_PROCESSOR, processor.getProcessorType())
        self.assertEquals("AMD Processor", processor.getProduct())
        self.assertEquals("abc123", processor.getSerial())
        self.assertEquals("AMD", processor.getVendor())
    
    def test_try_create_instance(self):
        self.assertRaises(RuntimeError, ProcessorImpl, {"test": "test"})