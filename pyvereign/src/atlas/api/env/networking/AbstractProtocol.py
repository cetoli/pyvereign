from atlas.api.env.networking.Protocol import Protocol

class AbstractProtocol(Protocol):
    
    def initialize(self):
        self.__name = ""
        self.__supportsBroadcasting = False
        self.__supportsMulticasting = False
        self.__guaranteesDelivery = False
        self.__guaranteesSequencing = False
        
    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name
        return self.__name
    
    def supportsBroadcasting(self):
        return self.__supportsBroadcasting
    
    def supportsMulticasting(self):
        return self.__supportsBroadcasting
    
    def guaranteesDelivery(self):
        return self.__guaranteesDelivery
    
    def guaranteesSequencing(self):
        return self.__guaranteesSequencing
    
    def setBroadcastingSupport(self, value):
        self.__supportsBroadcasting = value
        return self.__supportsBroadcasting
    
    def setMulticastingSupport(self, value):
        self.__supportsMulticasting = value
        return self.__supportsMulticasting
    
    def setDeliveryGuarantee(self, value):
        self.__guaranteesDelivery = value
        return self.__guaranteesDelivery
    
    def setSequencingGuarantee(self, value):
        self.__guaranteesSequencing = value
        return self.__guaranteesSequencing
        
    