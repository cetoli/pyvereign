from atlas.api.env.datasource.HardwareDataSource import HardwareDataSource

class AbstractHardwareDataSource(HardwareDataSource):
    
    def initialize(self):
        self._name = ""
    
    def getName(self):
        return self._name