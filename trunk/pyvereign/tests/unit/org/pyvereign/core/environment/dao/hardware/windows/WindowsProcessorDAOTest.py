from org.pyvereign.core.environment.dao.hardware.windows.WindowsProcessorDAO import WindowsProcessorDAO
import unittest

class WindowsProcessorDAOTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(WindowsProcessorDAO())
    
    def test_retrieve_processors(self):
        processors = WindowsProcessorDAO().retrieveProcessors()
        self.assertTrue(processors)
        self.assertTrue(len(processors) >= 1)
        