from atlas.api.env.service.HardwareService import HardwareService
from atlas.api.env.datasource.HardwareDataSource import HardwareDataSource

class AbstractHardwareService(HardwareService):
    
    def initialize(self, *params):
        self._dataSource = None
        
    def setDataSource(self, dataSource):
        if not dataSource:
            raise RuntimeError("None parameter")
        if not isinstance(dataSource, HardwareDataSource):
            raise TypeError("Invalid type")
        self._dataSource = dataSource
        return self._dataSource