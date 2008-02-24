from atlas.api.env.EnvironmentService import EnvironmentService

class AbstractEnvironmentService(EnvironmentService):
    
    def initialize(self, environment):
        self._name = ""
        self._environment = environment
        self._status = EnvironmentService.INITIALIZED
    
    def getStatus(self):
        return self._status
    
    def start(self, *params):
        self._status = EnvironmentService.STARTED
    
    def stop(self):
        self._status = EnvironmentService.STOPED
    
    def getName(self):
        return self._name
    
    def setDataSource(self, dataSource):
        self._dataSource = dataSource
        return self._dataSource