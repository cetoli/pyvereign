import win32com.client
strComputer = "."
objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator")
objSWbemServices = objWMIService.ConnectServer(strComputer,"root\cimv2")
colItems = objSWbemServices.ExecQuery("Select * from Win32_DisplayControllerConfiguration")
for objItem in colItems:
    print "Bits Per Pixel: ", objItem.BitsPerPixel
    print "Caption: ", objItem.Caption
    print "Color Planes: ", objItem.ColorPlanes
    print "Description: ", objItem.Description
    print "Device Entries In A Color Table: ", objItem.DeviceEntriesInAColorTable
    print "Device Specific Pens: ", objItem.DeviceSpecificPens
    print "Horizontal Resolution: ", objItem.HorizontalResolution
    print "Name: ", objItem.Name
    print "Refresh Rate: ", objItem.RefreshRate
    print "Reserved System Palette Entries: ", objItem.ReservedSystemPaletteEntries
    print "Setting ID: ", objItem.SettingID
    print "System Palette Entries: ", objItem.SystemPaletteEntries
    print "Vertical Resolution: ", objItem.VerticalResolution
    print "Video Mode: ", objItem.VideoMode