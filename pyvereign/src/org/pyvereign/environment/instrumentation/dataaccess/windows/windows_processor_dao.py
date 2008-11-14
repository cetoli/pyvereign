from org.pyvereign.base.object import Object
from win32com import client
from sets import ImmutableSet

class WindowsProcessorDAO(Object):
    
    def retrieveProcessors(self):
        strComputer = "."
        objWMIService = client.Dispatch("WbemScripting.SWbemLocator")
        objSWbemServices = objWMIService.ConnectServer(strComputer,"root\cimv2")
        colItems = objSWbemServices.ExecQuery("Select * from Win32_Processor")
        
        result = []
        
        if len(colItems):
            return ImmutableSet(result)
        
        
        
        