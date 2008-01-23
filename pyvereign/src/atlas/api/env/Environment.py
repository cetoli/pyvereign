from atlas.api.microkernel.AbstractInternalServer import AbstractInternalServer
from atlas.api.env.hardware.service.DefaultMachineService import DefaultMachineService

class Environment(AbstractInternalServer):
    
    def __init__(self):
        self.initialize()
        
    def initialize(self, *params):
        AbstractInternalServer.initialize(self, *params)
        
        machine = DefaultMachineService()
        
        from atlas.api.env.hardware.datasource.impl.windows.WindowsMachineDataSource import WindowsMachineDataSource
        
        self._services[machine.getName()] = machine
        
        machine.initialize()
        
        machine.setDataSource(WindowsMachineDataSource())
        
    
    def start(self, *params):
        for service in self._services.values():
            service.start()
    
    

