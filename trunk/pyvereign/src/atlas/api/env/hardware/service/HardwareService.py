from atlas.api.env.EnvironmentService import EnvironmentService

class HardwareService(EnvironmentService):
    
    def __init__(self):
        raise NotImplementedError()
    
    def setDataSource(self, dataSource):
        pass
    
    def initialize(self, *params):
        pass
    
    def start(self, *params):
        pass