from atlas.api.microkernel.AbstractInternalServer import AbstractInternalServer
from atlas.api.env.hardware.service.DefaultMachineService import DefaultMachineService
from atlas.api.env.hardware.datasource.impl.windows.WindowsMachineDataSource import WindowsMachineDataSource
from atlas.api.env.hardware.service.DefaultNetworkControllerService import DefaultNetworkControllerService
from atlas.api.env.hardware.datasource.impl.windows.WindowsNetworkControllerDataSource import WindowsNetworkControllerDataSource
from atlas.api.env.networking.service.DefaultProtocolService import DefaultProtocolService
from atlas.api.env.networking.datasource.impl.WindowsProtocolDataSource import WindowsProtocolDataSource

class Environment(AbstractInternalServer):
    
    def __init__(self):
        self.initialize()
        
    def initialize(self, *params):
        AbstractInternalServer.initialize(self, *params)
        
        machine = DefaultMachineService()
        self._services[machine.getName()] = machine
        machine.initialize()
        machine.setDataSource(WindowsMachineDataSource())
        
        networkController = DefaultNetworkControllerService()
        self._services[networkController.getName()] = networkController
        networkController.initialize()
        networkController.setDataSource(WindowsNetworkControllerDataSource())
        
        protocol = DefaultProtocolService()
        self._services[protocol.getName()] = protocol
        protocol.initialize()
        protocol.setDataSource(WindowsProtocolDataSource())
        
    
    def start(self, *params):
        for service in self._services.values():
            service.start()
    
    

