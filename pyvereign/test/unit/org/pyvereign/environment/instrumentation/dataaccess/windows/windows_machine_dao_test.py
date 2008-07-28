from org.pyvereign.base.interface import implements
from org.pyvereign.environment.instrumentation.hardware.imachine import IMachine
from org.pyvereign.environment.instrumentation.dataaccess.imachine_dao import IMachineDAO
import unittest
from org.pyvereign.environment.instrumentation.dataaccess.windows.windows_machine_dao import WindowsMachineDAO

class WindowsMachineDAOTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(WindowsMachineDAO())
        self.assertTrue(implements(WindowsMachineDAO(), IMachineDAO))
        
    def test_retrieve_machine(self):
        dao = WindowsMachineDAO()
        self.assertTrue(dao.retrieveMachine())
        self.assertTrue(implements(dao.retrieveMachine(), IMachine))
        
        machine = dao.retrieveMachine()
        
        self.assertTrue(machine.getDescription() <> "")
        self.assertTrue(machine.getDomain() <> "")
        self.assertTrue(machine.getHardwareId() <> "")
        self.assertTrue(machine.getLogicalName() <> "")
        self.assertTrue(machine.getNumberOfProcessors() >= 1)
        self.assertTrue(machine.getProduct() <> "")
        self.assertTrue(machine.getTotalPhysicalMemory() > 0)
        self.assertTrue(machine.getVendor() <> "")