from atlas.api.env.EnvironmentService import EnvironmentService

class AbstractEnvironmentService(EnvironmentService):
    
    def initialize(self, environment):
        self._name = ""
        self._environment = environment
    
    def getName(self):
        return self._name
    
    def setDataSource(self, dataSource):
        self._dataSource = dataSource
        return self._dataSource