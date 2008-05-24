import win32com.client
strComputer = "."
objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator")
objSWbemServices = objWMIService.ConnectServer(strComputer,"root\cimv2")
colItems = objSWbemServices.ExecQuery("Select * from Win32_NetworkProtocol")
for objItem in colItems:
    print "Caption: ", objItem.Caption
    print "Connectionless Service: ", objItem.ConnectionlessService
    print "Guarantees Delivery: ", objItem.GuaranteesDelivery
    print "Guarantees Sequencing: ", objItem.GuaranteesSequencing
    print "Install Date: ", objItem.InstallDate
    print "Maximum Address Size: ", objItem.MaximumAddressSize
    print "Maximum Message Size: ", objItem.MaximumMessageSize
    print "Message Oriented: ", objItem.MessageOriented
    print "Minimum Address Size: ", objItem.MinimumAddressSize
    print "Name: ", objItem.Name
    print "Pseudo Stream Oriented: ", objItem.PseudoStreamOriented
    print "Status: ", objItem.Status
    print "Supports Broadcasting: ", objItem.SupportsBroadcasting
    print "Supports Connect Data: ", objItem.SupportsConnectData
    print "Supports Disconnect Data: ", objItem.SupportsDisconnectData
    print "Supports Encryption: ", objItem.SupportsEncryption
    print "Supports Expedited Data: ", objItem.SupportsExpeditedData
    print "Supports Fragmentation: ", objItem.SupportsFragmentation
    print "Supports Graceful Closing: ", objItem.SupportsGracefulClosing
    print "Supports Guaranteed Bandwidth: ", objItem.SupportsGuaranteedBandwidth
    print "Supports Multicasting: ", objItem.SupportsMulticasting
    print "Supports Quality of Service: ", objItem.SupportsQualityofService