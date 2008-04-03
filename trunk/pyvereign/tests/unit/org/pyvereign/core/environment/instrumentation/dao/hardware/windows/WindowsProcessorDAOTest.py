from org.pyvereign.core.environment.instrumentation.dao.hardware.windows.WindowsProcessorDAO import WindowsProcessorDAO
import unittest

class WindowsProcessorDAOTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(WindowsProcessorDAO())
    
    def test_retrieve_processors(self):
        processors = WindowsProcessorDAO().retrieveProcessors()
        self.assertTrue(processors)
        self.assertTrue(len(processors) >= 1)
        
        for processor in processors:
            self.assertTrue(processor.getArchitecture())
            self.assertTrue(processor.getCPUStatus())
            self.assertTrue(processor.getCurrentClockSpeed())
            self.assertTrue(processor.getDescription())
            self.assertTrue(processor.getHardwareId())
            self.assertTrue(processor.getL2CacheSize())
            self.assertTrue(processor.getLoadPercentage())
            self.assertTrue(processor.getLogicalName())
            self.assertTrue(processor.getMaxClockSpeed())
            self.assertTrue(processor.getProcessorId())
            self.assertTrue(processor.getProcessorType())
            self.assertTrue(processor.getProduct())
            self.assertTrue(processor.getVendor())
        