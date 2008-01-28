from atlas.api.env.EnvironmentService import EnvironmentService

class AbstractEnvironmentService(EnvironmentService):
    
    def initialize(self):
        self._dataSource = None
    
    def setDataSource(self, dataSource):
        self._dataSource = dataSource
        return self._dataSource