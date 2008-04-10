from org.pyvereign.core.environment.transport.receiver.DatagramReceiver import DatagramReceiver
from org.pyvereign.core.environment.transport.receiver.StreamReceiver import StreamReceiver

class ReceiverFactory(object):
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
        self._receivers = {}
        self._receivers["UDP"] = DatagramReceiver
        self._receivers["TCP"] = StreamReceiver
    
    def createReceiver(self, protocolName, inetAddress, protocol):
        if not protocolName:
            raise RuntimeError("Invalid parameter.")
        if not isinstance(protocolName, str):
            raise TypeError("protocolName parameter is not an instance of str class.")
        return self._receivers[protocolName](inetAddress, protocol)