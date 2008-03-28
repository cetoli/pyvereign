import win32com.client
strComputer = "."
objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator")
objSWbemServices = objWMIService.ConnectServer(strComputer,"root\cimv2")
colItems = objSWbemServices.ExecQuery("Select * from Win32_PhysicalMemory")
for objItem in colItems:
    print "Bank Label: ", objItem.BankLabel
    print "Capacity: ", objItem.Capacity
    print "Caption: ", objItem.Caption
    print "Creation Class Name: ", objItem.CreationClassName
    print "Data Width: ", objItem.DataWidth
    print "Description: ", objItem.Description
    print "Device Locator: ", objItem.DeviceLocator
    print "Form Factor: ", objItem.FormFactor
    print "Hot Swappable: ", objItem.HotSwappable
    print "Install Date: ", objItem.InstallDate
    print "Interleave Data Depth: ", objItem.InterleaveDataDepth
    print "Interleave Position: ", objItem.InterleavePosition
    print "Manufacturer: ", objItem.Manufacturer
    print "Memory Type: ", objItem.MemoryType
    print "Model: ", objItem.Model
    print "Name: ", objItem.Name
    print "Other Identifying Info: ", objItem.OtherIdentifyingInfo
    print "Part Number: ", objItem.PartNumber
    print "Position In Row: ", objItem.PositionInRow
    print "Powered On: ", objItem.PoweredOn
    print "Removable: ", objItem.Removable
    print "Replaceable: ", objItem.Replaceable
    print "Serial Number: ", objItem.SerialNumber
    print "SKU: ", objItem.SKU
    print "Speed: ", objItem.Speed
    print "Status: ", objItem.Status
    print "Tag: ", objItem.Tag
    print "Total Width: ", objItem.TotalWidth
    print "Type Detail: ", objItem.TypeDetail
    print "Version: ", objItem.Version