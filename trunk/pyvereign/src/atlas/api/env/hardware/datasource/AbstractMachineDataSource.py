from atlas.api.env.hardware.datasource.MachineDataSource import MachineDataSource
from atlas.api.env.hardware.datasource.AbstractHardwareDataSource import AbstractHardwareDataSource

class AbstractMachineDataSource(AbstractHardwareDataSource, MachineDataSource):
    pass