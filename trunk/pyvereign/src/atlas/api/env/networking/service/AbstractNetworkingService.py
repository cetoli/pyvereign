from atlas.api.env.AbstractEnvironmentService import AbstractEnvironmentService
from atlas.api.env.networking.service.NetworkingService import NetworkingService
from atlas.api.env.networking.datasource.NetworkingDataSource import NetworkingDataSource

class AbstractNetworkingService(AbstractEnvironmentService, NetworkingService):
    
    def setDataSource(self, dataSource):
        if not dataSource:
            raise RuntimeError("None parameter")
        
        if not isinstance(dataSource, NetworkingDataSource):
            raise TypeError("Invalid type")
        return AbstractEnvironmentService.setDataSource(self, dataSource)