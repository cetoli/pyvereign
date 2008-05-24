import win32com.client
strComputer = "."
objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator")
objSWbemServices = objWMIService.ConnectServer(strComputer,"root\cimv2")
colItems = objSWbemServices.ExecQuery("Select * from Win32_Battery")
for objItem in colItems:
    print objItem.Name
    print objItem.Caption
    print objItem.Description
    print objItem.DeviceId
    print objItem.EstimatedChargeRemaining
    print objItem.EstimatedRunTime
    print objItem.ExpectedBatteryLife