from org.pyvereign.base.interface import Interface

class IProcessorDAO(object):
    
    __metaclass__ = Interface
    
    def __init__(self):
        raise NotImplementedError()
    
    def retrieveProcessors(self):
        raise NotImplementedError()