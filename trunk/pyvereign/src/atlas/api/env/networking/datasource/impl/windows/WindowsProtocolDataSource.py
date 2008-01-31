from atlas.api.env.networking.datasource.AbstractProtocolDataSource import AbstractProtocolDataSource
from win32com import client
from atlas.api.env.networking.DefaultProtocol import DefaultProtocol

class WindowsProtocolDataSource(AbstractProtocolDataSource):
    
    def __init__(self):
        self.initialize()
        
    def initialize(self):
        AbstractProtocolDataSource.initialize(self)
        self._name = "WindowsProtocolDataSource"
    
    def retrieveProtocols(self):
        strComputer = "."
        objWMIService = client.Dispatch("WbemScripting.SWbemLocator")
        objSWbemServices = objWMIService.ConnectServer(strComputer,"root\cimv2")
        colItems = objSWbemServices.ExecQuery("Select * from Win32_NetworkProtocol where Name like '%/IP%'")
        protocols = []
        for objItem in colItems:
            protocol = DefaultProtocol()
            if str(objItem.Name).find("UDP") > -1:
                protocol.setName("UDP")
            elif str(objItem.Name).find("TCP") > -1:
                protocol.setName("TCP")
            
            protocol.setBroadcastingSupport(bool(objItem.SupportsBroadcasting))
            protocol.setDeliveryGuarantee(bool(objItem.GuaranteesDelivery))
            protocol.setMulticastingSupport(bool(objItem.SupportsMulticasting))
            protocol.setSequencingGuarantee(bool(objItem.GuaranteesSequencing))
            
            protocols.append(protocol)
        
        return protocols
