from org.pyvereign.base.interface import Interface

class IMachineDAO(object):
    
    __metaclass__ = Interface
    
    def __init__(self):
        raise NotImplementedError()
    
    def retrieveMachineDAO(self):
        raise NotImplementedError()