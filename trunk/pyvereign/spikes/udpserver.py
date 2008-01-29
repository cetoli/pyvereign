from atlas.api.env.transport.communicationapi.DatagramSocketAdapter import DatagramSocketAdapter
from atlas.api.env.transport.communicationapi.BindIPv4Address import BindIPv4Address
from atlas.api.env.transport.communicationapi.IPv4Address import IPv4Address

adapter = DatagramSocketAdapter(IPv4Address('', 5050))
adapter.open()
while True:
    
    stream = adapter.receive(1024)
    if stream:
        print stream