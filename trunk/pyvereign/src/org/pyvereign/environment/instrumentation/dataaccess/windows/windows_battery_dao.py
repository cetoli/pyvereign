from win32com import client
from org.pyvereign.base.object import Object
from org.pyvereign.util.decorators.public import public
from org.pyvereign.environment.instrumentation.hardware.hardware_factory import HardwareFactory
from org.pyvereign.util.decorators.return_type import return_type
from org.pyvereign.environment.instrumentation.hardware.ibattery import IBattery

class WindowsBatteryDAO(Object):
    
    @public
    @return_type(IBattery)
    def retrieveBattery(self):
        strComputer = "."
        objWMIService = client.Dispatch("WbemScripting.SWbemLocator")
        objSWbemServices = objWMIService.ConnectServer(strComputer,"root\cimv2")
        colItems = objSWbemServices.ExecQuery("Select * from Win32_Battery")
        
        battery = battery = HardwareFactory.createBattery()
        
        if len(colItems) == 0:
            battery.setEstimatedChargeRemaining(100)
            return battery
            
        item = colItems[0]
        
        battery.setDescription(item.Description)
        battery.setEstimatedChargeRemaining(int(item.EstimatedChargeRemaining))
        battery.setHardwareId(str(item.DeviceId))
        battery.setLogicalName(str(item.Caption))
        battery.setProduct(str(item.Caption))
        battery.setSerial(str(item.DeviceId))
            
        return battery

