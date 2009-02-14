from org.pyvereign.base.object import Object
from org.pyvereign.util.decorators.return_type import return_type
from org.pyvereign.util.decorators.require import require
from org.pyvereign.util.decorators.pre_condition import pre_condition
from org.pyvereign.error.inet_address_error import InetAddressError
from org.pyvereign.util.decorators.public import public

class AbstractInetAddress(Object):
    
    def __init__(self):
        raise NotImplementedError()
    
    @return_type(None)
    @pre_condition("family", lambda family: family >= 0, InetAddressError, "Invalid family")
    @require("family", int)
    def setFamily(self, family):
        self.__family
    
    @public
    @return_type(int)    
    def getFamily(self):
        return self.__family
    
    @return_type(None)
    def setIPAddress(self, ipaddress):
        self.__ipaddress
    
    def getIPAddress(self):
        pass
    
    def getPort(self):
        pass
    
    def getTuple(self):
        pass
    
    def isBroadcastAddress(self):
        pass
    
    def isBindAddress(self):
        pass
    
    def setPort(self, port):
        pass