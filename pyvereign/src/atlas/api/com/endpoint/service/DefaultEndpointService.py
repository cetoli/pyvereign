from atlas.api.com.endpoint.service.AbstractEndpointService import AbstractEndpointService

class DefaultEndpointService(AbstractEndpointService):
    
    def __init__(self):
        self._status = DefaultEndpointService.NON_INITIALIZED