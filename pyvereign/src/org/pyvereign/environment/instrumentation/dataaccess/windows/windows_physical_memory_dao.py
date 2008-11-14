from org.pyvereign.base.object import Object
from win32com import client
from org.pyvereign.util.decorators.public import public
from org.pyvereign.util.decorators.return_type import return_type
from sets import ImmutableSet
from org.pyvereign.environment.instrumentation.hardware.hardware_factory import HardwareFactory

class WindowsPhysicalMemoryDAO(Object):
    
    @public
    @return_type(ImmutableSet)
    def retrievePhysicalMemories(self):
        strComputer = "."
        objWMIService = client.Dispatch("WbemScripting.SWbemLocator")
        objSWbemServices = objWMIService.ConnectServer(strComputer,"root\cimv2")
        colItems = objSWbemServices.ExecQuery("Select * from Win32_PhysicalMemory")
        
        result = []
        
        if len(colItems) == 0:
            return ImmutableSet(result)
        
        for item in colItems:
            memory = HardwareFactory.createPhysicalMemory()
            memory.setCapacity(int(item.Capacity))
            result.append(memory)
            
        return ImmutableSet(result)