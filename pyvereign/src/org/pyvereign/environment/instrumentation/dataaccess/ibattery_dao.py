from org.pyvereign.base.interface import Interface

class IBatteryDAO(object):
    
    __metaclass__ = Interface
    
    
    def __init__(self):
        raise NotImplementedError()
    
    def retrieveBattery(self):
        raise NotImplementedError()