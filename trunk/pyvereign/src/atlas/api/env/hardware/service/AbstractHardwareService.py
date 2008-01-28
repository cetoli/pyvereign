from atlas.api.env.hardware.service.HardwareService import HardwareService
from atlas.api.env.hardware.datasource.HardwareDataSource import HardwareDataSource
from atlas.api.env.AbstractEnvironmentService import AbstractEnvironmentService

class AbstractHardwareService(AbstractEnvironmentService, HardwareService):
    
    def setDataSource(self, dataSource):
        if not dataSource:
            raise RuntimeError("None parameter")
        
        if not isinstance(dataSource, HardwareDataSource):
            raise TypeError("Invalid type")
        return AbstractEnvironmentService.setDataSource(self, dataSource)