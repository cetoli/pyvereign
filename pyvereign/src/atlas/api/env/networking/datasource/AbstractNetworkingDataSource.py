from atlas.api.env.AbstractEnvironmentDataSource import AbstractEnvironmentDataSource
from atlas.api.env.networking.datasource.NetworkingDataSource import NetworkingDataSource

class AbstractNetworkingDataSource(AbstractEnvironmentDataSource, NetworkingDataSource):
    pass