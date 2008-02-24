from atlas.api.env.networking.service.AbstractProtocolService import AbstractProtocolService

class DefaultProtocolService(AbstractProtocolService):
    
    def __init__(self):
        self._status = DefaultProtocolService.NON_INITIALIZED