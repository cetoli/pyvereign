from org.pyvereign.core.environment.instrumentation.dto.system.ProcessImpl import ProcessImpl
import unittest

class ProcessImplTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(ProcessImpl({}))
        
        values = {"name": "test", "maximumWorkingSetSize": 1402, 
                  "minimumWorkingSetSize": 2048, "processId": "123456",
                  "virtualSize": 145}
        
        process = ProcessImpl(values)
        self.assertEquals("test", process.getName())
        self.assertEquals(1402, process.getMaximumWorkingSetSize())
        self.assertEquals(2048, process.getMinimumWorkingSetSize())
        self.assertEquals("123456", process.getProcessId())
        self.assertEquals(145, process.getVirtualSize())
        
    def test_try_create_instance(self):
        self.assertRaises(RuntimeError, ProcessImpl, {"test": 1})