from atlas.api.env.datasource.MachineDataSource import MachineDataSource
from atlas.api.env.datasource.AbstractHardwareDataSource import AbstractHardwareDataSource

class AbstractMachineDataSource(AbstractHardwareDataSource, MachineDataSource):
    pass