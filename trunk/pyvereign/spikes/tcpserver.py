from atlas.api.env.transport.receiver.StreamReceiver import StreamReceiver
from atlas.api.env.transport.address.BindIPv4Address import BindIPv4Address
from atlas.api.env.networking.DefaultProtocol import DefaultProtocol
from atlas.api.exception.TransportError import TransportError
from atlas.api.exception.BindError import BindError
try:
    receiver = StreamReceiver(BindIPv4Address(5050), DefaultProtocol())
    receiver.open()
    receiver.bind()
    while True:
        data = receiver.receive()
        if data:
            print data
except (TransportError, BindError), e:
    print e
    receiver.close()