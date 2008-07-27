from org.pyvereign.base.interface import Interface

class INetworkAdapterDAO(object):
    
    __metaclass__ = Interface
    
    def __init__(self):
        raise NotImplementedError()
    
    def retrieveNetworkAdapters(self):
        raise NotImplementedError()