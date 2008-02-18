from atlas.api.env.transport.address.IPv4Address import IPv4Address
from atlas.api.env.transport.address.BindIPv4Address import BindIPv4Address
from atlas.api.env.transport.address.BroadcastIPv4Address import BroadcastIPv4Address

class InetAddressFactory(object):
    
    def createInetAddress(self, ipAddress, port):
        return IPv4Address(ipAddress, port)
    
    def createBindAddress(self, port):
        return BindIPv4Address(port)
    
    def createBroadcastAddress(self, port):
        return BroadcastIPv4Address(port)
    
    createInetAddress = classmethod(createInetAddress)
    createBindAddress = classmethod(createBindAddress)
    createBroadcastAddress = classmethod(createBroadcastAddress)
    