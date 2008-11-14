from org.pyvereign.base.interface import Interface

class IPhysicalMemoryDAO(object):
    
    __metaclass__ = Interface
    
    def __init__(self):
        raise NotImplementedError()
    
    def retrievePhysicalMemories(self):
        raise NotImplementedError()