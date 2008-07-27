from org.pyvereign.base.interface import Interface

class IPhysicalMemodryDAO(object):
    
    __metaclass__ = Interface
    
    def __init__(self):
        raise NotImplementedError()
    
    def retrievePhysicalMemories(self):
        raise NotImplementedError()