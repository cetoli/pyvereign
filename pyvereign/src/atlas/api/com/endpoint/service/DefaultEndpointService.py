from atlas.api.com.endpoint.service.AbstractEndpointService import AbstractEndpointService

class DefaultEndpointService(AbstractEndpointService):
    
    def __init__(self):
        self._name = "endpoint"