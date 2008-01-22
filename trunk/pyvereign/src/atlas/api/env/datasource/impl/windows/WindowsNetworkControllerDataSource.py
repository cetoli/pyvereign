from atlas.api.env.datasource.AbstractNetworkControllerDataSource import AbstractNetworkControllerDataSource
from win32com import client
from atlas.api.env.hardware.DefaultNeworkController import DefaultNetworkController

class WindowsNetworkControllerDataSource(AbstractNetworkControllerDataSource):
    
    def __init__(self):
        self.initialize()
    
    def initialize(self):
        AbstractNetworkControllerDataSource.initialize(self)
        self._name = "WindowsNetworkControllerDataSource"
    
    def retrieveNetworkControllers(self):
        controllers = []
        
        strComputer = "."
        objWMIService = client.Dispatch("WbemScripting.SWbemLocator")
        objSWbemServices = objWMIService.ConnectServer(strComputer,"root\cimv2")
        colItems = objSWbemServices.ExecQuery("Select * from Win32_NetworkAdapterConfiguration where DNSHostName <> null")
        
        for item in colItems:
            controller = DefaultNetworkController()
            controller.setDescription(str(item.Description))
            controller.setHardwareId(str(item.Index))
            controller.setIPAddress(str(item.IPAddress[0]))
            
            adapters = objSWbemServices.ExecQuery("Select * from Win32_NetworkAdapter where Index = " + controller.getHardwareId())             
            
            adapter = adapters[0]
            
            controller.setLogicalName(str(adapter.Name))
            controller.setMACAddress(str(adapter.MACAddress))
            
            if not adapter.MaxSpeed:
                if str(adapter.Name).find("802.11") > -1 or str(adapter.Name).find("wireless") > -1 or str(adapter.Name).find("Wireless") > -1:
                    controller.setMaxSpeed(11)
                else:
                    controller.setMaxSpeed(100)
            else:
                controller.setMaxSpeed(int(adapter.MaxSpeed))
                
            controller.setProduct(str(adapter.ProductName))
            controller.setSerial(str(adapter.MACAddress))
            controller.setVendor(str(adapter.Manufacturer))
            
            controllers.append(controller)
        
        return controllers