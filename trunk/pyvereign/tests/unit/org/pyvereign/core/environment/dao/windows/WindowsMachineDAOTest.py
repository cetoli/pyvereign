from org.pyvereign.core.environment.dao.hardware.windows.WindowsMachineDAO import WindowsMachineDAO
import unittest

class WindowsMachineDAOTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(WindowsMachineDAO())
    
    def test_retrieve_machine(self):
        machine = WindowsMachineDAO().retrieveMachine()
        
        self.assertTrue(machine.getDescription() <> "")
        self.assertTrue(machine.getDomain() <> "")
        self.assertTrue(machine.getHardwareId() <> "")
        self.assertTrue(machine.getLogicalName() <> "")
        self.assertTrue(machine.getNumberOfProcessors() >= 1)
        self.assertTrue(machine.getProduct() <> "")
        self.assertTrue(machine.getTotalPhysicalMemory() > 0)
        self.assertTrue(machine.getVendor() <> "")