class CommunicationAPIAdapterFactory(object):
    
    def __new__(cls):
        if not 'instance' in cls.__dict__:
            cls.instance = object.__new__(cls)
            cls.instance.initialize()
        return cls.instance
    
    def initialize(self):
        self.__adapters = {}
    
    def createCommunicationAPIAdapterFactory(self, protocolName):
        return self.__adapters[protocolName]()
    
    def registerCommunicationAPIAdapterClass(self, name, clazz):
        self.__adapters[name] = clazz
        return self.__adapters[name]
    
    def unregisterCommunicationAPIAdapterClass(self, name):
        adapter = self.__adapters[name]
        del self.__adapters[name]
        return adapter