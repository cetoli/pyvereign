class EnvironmentService(object):
    
    def __init__(self):
        raise NotImplementedError()
    
    def initialize(self, environment):
        pass
    
    def start(self, *params):
        pass
    
    def setDataSource(self, dataSource):
        pass
    
    def getName(self):
        pass
    
    def stop(self):
        pass