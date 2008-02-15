from atlas.api.env.transport.receiver.StreamReceiver import StreamReceiver
from atlas.api.env.transport.address.BindIPv4Address import BindIPv4Address
from atlas.api.env.networking.DefaultProtocol import DefaultProtocol
from atlas.api.exception.TransportError import TransportError
from atlas.api.exception.BindError import BindError
from atlas.api.env.transport.listener.StreamListener import StreamListener
from atlas.api.env.Environment import Environment
from atlas.api.env.transport.listener.TransportListener import TransportListener

class DefaultListener(TransportListener):
    
    def __init__(self):
        print "what!?!?!?!?!?!?!?!?"
    
    def processStream(self, stream):
        print stream

environment = Environment()
environment.initialize()
environment.start()

try:
    receiver = StreamReceiver(BindIPv4Address(5050), DefaultProtocol())
    listener = StreamListener(environment, receiver)
    listener.addTransportListener(DefaultListener())
    listener.open()
    listener.start()
except (TransportError, BindError), e:
    print e
    listener.close()