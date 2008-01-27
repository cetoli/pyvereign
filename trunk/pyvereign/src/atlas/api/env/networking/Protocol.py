
class Protocol(object):
    
    def __init__(self):
        raise NotImplementedError()
    
    def getName(self):
        pass
    
    def setName(self, name):
        pass
    
    def supportsBroadcasting(self):
        pass
    
    def supportsMulticasting(self):
        pass
    
    def guaranteesDelivery(self):
        pass
    
    def guaranteesSequencing(self):
        pass
    
    def setBroadcastingSupport(self, value):
        pass
    
    def setMulticastingSupport(self, value):
        pass
    
    def setDeliveryGuarantee(self, value):
        pass
    
    def setSequencingGuarantee(self, value):
        pass