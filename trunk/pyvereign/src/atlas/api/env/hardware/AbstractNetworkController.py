from atlas.api.env.hardware.AbstractHardware import AbstractHardware
from atlas.api.env.hardware.NetworkController import NetworkController

class AbstractNetworkController(AbstractHardware, NetworkController):
    
    def initialize(self):
        AbstractHardware.initialize(self)
        self._macAddress = ""
        self._isConnected = False
        self._maxSpeed = 0
        self._speed = 0
        self._ipAddress = ""
    
    def setMACAddress(self, macAddress):
        if not macAddress:
            raise RuntimeError("None parameter")
        if not isinstance(macAddress, str):
            raise TypeError("Invalid data type.")
        self._macAddress = macAddress
        return self._macAddress
    
    def getMACAddress(self):
        return self._macAddress
    
    def isConnected(self):
        self._isConnected
        
    def connected(self):
        self._isConnected = True
    
    def disconnected(self):
        self._isConnected = False
    
    def setMaxSpeed(self, maxSpeed):
        if not maxSpeed:
            raise RuntimeError("None parameter")
        if not isinstance(maxSpeed, int):
            raise TypeError("Invalid data type.")
        if maxSpeed < 1:
            raise RuntimeError("Invalid value.")
        self._maxSpeed = maxSpeed
        return self._maxSpeed
    
    def getMaxSpeed(self):
        return self._maxSpeed
    
    def setSpeed(self, speed):
        if not speed:
            raise RuntimeError("None parameter")
        if not isinstance(speed, int):
            raise TypeError("Invalid data type.")
        if speed < 1:
            raise RuntimeError("Invalid value.")
        self._speed = speed
        return self._speed
    
    def getSpeed(self):
        return self._speed
    
    def setIPAddress(self, ipAddress):
        if not ipAddress:
            raise RuntimeError("None parameter")
        if not isinstance(ipAddress, str):
            raise TypeError("Invalid data type.")
        self._ipAddress = ipAddress
        return self._ipAddress
    
    def getIPAddress(self):
        return self._ipAddress