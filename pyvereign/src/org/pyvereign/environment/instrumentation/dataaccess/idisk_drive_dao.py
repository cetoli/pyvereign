from org.pyvereign.base.interface import Interface

class IDiskDriveDAO(object):
    
    __metaclass__ = Interface
    
    def __init__(self):
        raise NotImplementedError()
    
    def retrieveDiskDrives(self):
        raise NotImplementedError()
    