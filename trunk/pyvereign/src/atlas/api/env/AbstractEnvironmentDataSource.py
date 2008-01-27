from atlas.api.env.EnvironmentDataSource import EnvironmentDataSource

class AbstractEnvironmentDataSource(EnvironmentDataSource):
    
    def initialize(self):
        self._name = ""
    
    def getName(self):
        return self._name