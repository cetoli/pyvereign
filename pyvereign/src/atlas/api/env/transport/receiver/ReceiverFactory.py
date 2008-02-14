from atlas.api.env.transport.receiver.DatagramReceiver import DatagramReceiver
from atlas.api.env.transport.receiver.StreamReceiver import StreamReceiver
class ReceiverFactory(object):
    
    def __new__(cls):
        if not 'instance' in cls.__dict__:
            cls.instance = object.__new__(cls)
            cls.instance.initialize()
        return cls.instance
    
    def initialize(self):
        self._receivers = {}
        self._receivers["UDP"] = DatagramReceiver
        self._receivers["TCP"] = StreamReceiver
    
    def createForwarder(self, protocolName, inetAddress, protocol):
        if not protocolName:
            raise RuntimeError("Invalid parameter.")
        if not isinstance(protocolName, str):
            raise TypeError("protocolName parameter is not an instance of str class.")
        return self._receivers[protocolName](inetAddress, protocol)