class HardwareFactory(object):
    
    def __new__(cls):
        if not 'instance' in cls.__dict__:
            cls.instance = object.__new__(cls)
        
        return cls.instance
    
    