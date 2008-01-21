from atlas.api.env.datasource.AbstractMachineDataSource import AbstractMachineDataSource
from atlas.api.env.hardware.DefaultMachine import DefaultMachine
from win32com import client

class WindowsMachineDataSource(AbstractMachineDataSource):
    
    def __init__(self):
        self.initialize()
    
    def initialize(self):
        AbstractMachineDataSource.initialize(self)
        self._name = "WindowsMachineDataSource"
    
    def retrieveMachine(self):
        machine = DefaultMachine()
        
        strComputer = "."
        objWMIService = client.Dispatch("WbemScripting.SWbemLocator")
        objSWbemServices = objWMIService.ConnectServer(strComputer,"root\cimv2")
        colItems = objSWbemServices.ExecQuery("Select * from Win32_ComputerSystem")
        
        if len(colItems) <> 1:
            raise Exception()
        
        objItem = colItems[0]
        
        machine.setDescription(str(objItem.Description))
        machine.setDomain(str(objItem.Domain))
        machine.setId(str(objItem.Name))
        machine.setLogicalName(str(objItem.Name))
        machine.setNumberOfProcessors(int(objItem.NumberOfProcessors))
        machine.setProduct(str(objItem.Model))
        machine.setSerial(str(objItem.Model))
        machine.setTotalPhysicalMemory(int(objItem.TotalPhysicalMemory))
        machine.setVendor(str(objItem.Manufacturer))
        
        return machine