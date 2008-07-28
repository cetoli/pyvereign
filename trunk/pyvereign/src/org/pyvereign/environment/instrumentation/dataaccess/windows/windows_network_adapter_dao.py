from org.pyvereign.base.object import Object
from win32com import client
from org.pyvereign.environment.instrumentation.hardware.hardware_factory import HardwareFactory
from sets import ImmutableSet

class WindowsNetworkAdapterDAO(Object):
    
    def retrieveNetworkAdapters(self):
        strComputer = "."
        objWMIService = client.Dispatch("WbemScripting.SWbemLocator")
        objSWbemServices = objWMIService.ConnectServer(strComputer,"root\cimv2")
        colItems = objSWbemServices.ExecQuery("Select * from Win32_NetworkAdapterConfiguration where DNSHostName <> null")
        
        result = []
        
        if len(colItems) == 0:
            return ImmutableSet(result)
        
        for item in colItems:
            adapters = objSWbemServices.ExecQuery("Select * from Win32_NetworkAdapter where Index = " + str(item.Index))             
            adapter = adapters[0]
            
            networkAdapter = HardwareFactory.createNetworkAdapter()
            
            networkAdapter.setDescription(str(adapter.Description))
            networkAdapter.setHardwareId(str(adapter.DeviceId))
            networkAdapter.setIPAddress(str(item.IPAddress[0]))
            networkAdapter.setLogicalName(str(adapter.Name))
            networkAdapter.setMACAddress(str(adapter.MACAddress))
            networkAdapter.setProduct(str(adapter.Name))
            networkAdapter.setSerial(str(adapter.DeviceId))
            networkAdapter.setSpeed(int(adapter.Speed))
            networkAdapter.setVendor(str(adapter.Manufacturer))
            
            result.append(networkAdapter)
        
        return ImmutableSet(result)