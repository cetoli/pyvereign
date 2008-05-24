import win32com.client
strComputer = "."
objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator")
objSWbemServices = objWMIService.ConnectServer(strComputer,"root\cimv2")
colItems = objSWbemServices.ExecQuery("Select * from Win32_LogicalDisk")
for objItem in colItems:
    print "Access: ", objItem.Access
    print "Availability: ", objItem.Availability
    print "Block Size: ", objItem.BlockSize
    print "Caption: ", objItem.Caption
    print "Compressed: ", objItem.Compressed
    print "Config Manager Error Code: ", objItem.ConfigManagerErrorCode
    print "Config Manager User Config: ", objItem.ConfigManagerUserConfig
    print "Creation Class Name: ", objItem.CreationClassName
    print "Description: ", objItem.Description
    print "Device ID: ", objItem.DeviceID
    print "Drive Type: ", objItem.DriveType
    print "Error Cleared: ", objItem.ErrorCleared
    print "Error Description: ", objItem.ErrorDescription
    print "Error Methodology: ", objItem.ErrorMethodology
    print "File System: ", objItem.FileSystem
    print "Free Space: ", objItem.FreeSpace
    print "Install Date: ", objItem.InstallDate
    print "Last Error Code: ", objItem.LastErrorCode
    print "Maximum Component Length: ", objItem.MaximumComponentLength
    print "Media Type: ", objItem.MediaType
    print "Name: ", objItem.Name
    print "Number Of Blocks: ", objItem.NumberOfBlocks
    print "PNP Device ID: ", objItem.PNPDeviceID
    z = objItem.PowerManagementCapabilities
    if z is None:
        a = 1
    else:
        for x in z:
            print "Power Management Capabilities: ", x
    print "Power Management Supported: ", objItem.PowerManagementSupported
    print "Provider Name: ", objItem.ProviderName
    print "Purpose: ", objItem.Purpose
    print "Quotas Disabled: ", objItem.QuotasDisabled
    print "Quotas Incomplete: ", objItem.QuotasIncomplete
    print "Quotas Rebuilding: ", objItem.QuotasRebuilding
    print "Size: ", objItem.Size
    print "Status: ", objItem.Status
    print "Status Info: ", objItem.StatusInfo
    print "Supports Disk Quotas: ", objItem.SupportsDiskQuotas
    print "Supports File-Based Compression: ", objItem.SupportsFileBasedCompression
    print "System Creation Class Name: ", objItem.SystemCreationClassName
    print "System Name: ", objItem.SystemName
    print "Volume Dirty: ", objItem.VolumeDirty
    print "Volume Name: ", objItem.VolumeName
    print "Volume Serial Number: ", objItem.VolumeSerialNumber