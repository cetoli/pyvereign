from atlas.api.env.transport.communicationapi.BindIPv4Address import BindIPv4Address
from atlas.api.env.transport.communicationapi.StreamSocketAdapter import StreamSocketAdapter

adapter = StreamSocketAdapter(BindIPv4Address(5050))
adapter.open()
while True:
    
    stream = adapter.receive(1024)
    if stream:
        print stream