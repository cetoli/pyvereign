from org.pyvereign.base.object import Object
from win32com import client
from org.pyvereign.util.decorators.public import public
from org.pyvereign.util.decorators.return_type import return_type
from org.pyvereign.environment.instrumentation.hardware.imachine import IMachine
from org.pyvereign.error.dao_error import DAOError
from org.pyvereign.environment.instrumentation.hardware.hardware_factory import HardwareFactory

class WindowsMachineDAO(Object):
    
    @public
    @return_type(IMachine)
    def retrieveMachine(self):
        strComputer = "."
        objWMIService = client.Dispatch("WbemScripting.SWbemLocator")
        objSWbemServices = objWMIService.ConnectServer(strComputer,"root\cimv2")
        colItems = objSWbemServices.ExecQuery("Select * from Win32_ComputerSystem")
        
        if len(colItems) == 0:
            raise DAOError()
        
        item = colItems[0]
        
        machine = HardwareFactory.createMachine()
        machine.setDescription(str(item.Description))
        machine.setDomain(str(item.Domain))
        machine.setHardwareId(str(item.Name))
        machine.setLogicalName(str(item.Name))
        machine.setNumberOfProcessors(int(item.NumberOfProcessors))
        machine.setProduct(str(item.Model))
        machine.setTotalPhysicalMemory(int(item.TotalPhysicalMemory))
        machine.setVendor(str(item.Manufacturer))
        
        return machine