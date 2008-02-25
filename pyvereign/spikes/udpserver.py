from atlas.api.exception.TransportError import TransportError
from atlas.api.exception.BindError import BindError
from atlas.api.env.transport.listener.TransportListener import TransportListener
from atlas.api.microkernel.Microkernel import Microkernel

class DefaultListener(TransportListener):
    
    def __init__(self):
        print "what!?!?!?!?!?!?!?!?"
    
    def processStream(self, stream):
        print stream

try:
    Microkernel().initialize()
    Microkernel().start(5050)
    Microkernel().executeMecanism("Environment", "transport", "addTransportListener", "UDP", "UDP://127.0.0.1:5050", DefaultListener())
except (TransportError, BindError), e:
    print e
    Microkernel().stop()
    

