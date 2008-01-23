from atlas.api.env.hardware.AbstractNetworkController import AbstractNetworkController

class DefaultNetworkController(AbstractNetworkController):
    
    def __init__(self):
        self.initialize()