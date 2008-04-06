from org.pyvereign.core.environment.transport.forwarder.DatagramForwarder import DatagramForwarder
from org.pyvereign.core.environment.transport.forwarder.StreamForwarder import StreamForwarder

class ForwarderFactory(object):
    
    def __new__(cls):
        if not 'instance' in cls.__dict__:
            cls.instance = object.__new__(cls)
            cls.instance.initialize()
        return cls.instance
    
    def initialize(self):
        self._forwarders = {}
        self._forwarders["UDP"] = DatagramForwarder
        self._forwarders["TCP"] = StreamForwarder
        
    def createForwarder(self, protocolName, inetAddress, protocol):
        if not protocolName:
            raise RuntimeError("Invalid parameter.")
        if not isinstance(protocolName, str):
            raise TypeError("protocolName parameter is not an instance of str class.")
        return self._forwarders[protocolName](inetAddress, protocol)