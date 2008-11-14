from org.pyvereign.base.object import Object
from win32com import client
from sets import ImmutableSet
from org.pyvereign.util.decorators.public import public

class WindowsProcessorDAO(Object):
    
    @public
    def retrieveProcessors(self):
        strComputer = "."
        objWMIService = client.Dispatch("WbemScripting.SWbemLocator")
        objSWbemServices = objWMIService.ConnectServer(strComputer,"root\cimv2")
        colItems = objSWbemServices.ExecQuery("Select * from Win32_Processor")
        
        result = []
        
        if len(colItems):
            return ImmutableSet(result)
        
        
        
        