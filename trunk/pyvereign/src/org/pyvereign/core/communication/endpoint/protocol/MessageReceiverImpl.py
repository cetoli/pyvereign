from org.pyvereign.core.communication.endpoint.protocol.AbstractMessageReceiver import AbstractMessageReceiver
class MessageReceiverImpl(AbstractMessageReceiver):
    
    def __init__(self, endpointAddress, kernel):
        self.init(endpointAddress, kernel)