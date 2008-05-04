from org.pyvereign.core.environment.transport.forwarder.DatagramForwarder import DatagramForwarder
from org.pyvereign.core.environment.transport.forwarder.StreamForwarder import StreamForwarder

class ForwarderFactory(object):
    """
    Defines the implementation of the factory for Forwarder object creation.
    
    @author: Fabricio
    @since: 
    @version: 0.0.1
    """
    
    def __new__(cls):
        if not 'instance' in cls.__dict__:
            cls.instance = object.__new__(cls)
            cls.instance.init()
        return cls.instance
    
    def init(self):
        self._forwarders = {}
        self._forwarders["UDP"] = DatagramForwarder
        self._forwarders["TCP"] = StreamForwarder
        
    def createForwarder(self, protocolName, inetAddress, protocol):
        if not protocolName:
            raise RuntimeError("Invalid parameter.")
        if not isinstance(protocolName, str):
            raise TypeError("protocolName parameter is not an instance of str class.")
        return self._forwarders[protocolName](inetAddress, protocol)