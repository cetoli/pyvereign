from atlas.api.env.hardware.AbstractHardware import AbstractHardware
from atlas.api.env.hardware.NetworkController import NetworkController

class AbstractNetworkController(AbstractHardware, NetworkController):
    
    def initialize(self):
        AbstractHardware.initialize(self)
        self._macAddress = ""
        self._isConnected = False
        self._maxSpeed = 0
        self._speed = 0
    
    def setMACAddress(self, macAddress):
        self._macAddress = macAddress
        return self._macAddress
    
    def getMACAddress(self):
        return self._macAddress
    
    def isConnected(self):
        self._isConnected
    
    def setMaxSpeed(self, maxSpeed):
        self._maxSpeed = maxSpeed
        return self._maxSpeed
    
    def getMaxSpeed(self):
        return self._maxSpeed
    
    def setSpeed(self, speed):
        self._speed = speed
        return self._speed
    
    def getSpeed(self):
        return self._speed