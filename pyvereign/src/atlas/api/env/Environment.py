from atlas.api.microkernel.InternalServer import InternalServer
from atlas.api.env.service.DefaultMachineService import DefaultMachineService
from atlas.api.env.datasource.impl.windows.WindowsMachineDataSource import WindowsMachineDataSource
from atlas.api.env.service.DefaultNetworkControllerService import DefaultNetworkControllerService
from atlas.api.env.datasource.impl.windows.WindowsNetworkControllerDataSource import WindowsNetworkControllerDataSource

class Environment(InternalServer):
    
    def __init__(self):
        self._services = {}
        
        service = DefaultMachineService()
        service.initialize()
        service.setDataSource(WindowsMachineDataSource())
        service.start()
        print service.getDescription()
        
        self._services[service.getName()] = service
        
        service = DefaultNetworkControllerService()
        service.initialize()
        service.setDataSource(WindowsNetworkControllerDataSource())
        service.start()
        
        self._services[service.getName()] = service
    
    def executeService(self, serviceName, action, *params):
        print params
        return self._services[serviceName].__getattribute__(action)(*params)

print Environment().executeService("MachineService", "getHardwareId")