from org.pyvereign.core.environment.transport.address.IPv4Address import IPv4Address
from org.pyvereign.core.environment.transport.address.BindIPv4Address import BindIPv4Address
from org.pyvereign.core.environment.transport.address.BroadcastIPv4Address import BroadcastIPv4Address

class InetAddressFactory(object):
    
    def createInetAddress(self, ipAddress, port, type = None):
        return IPv4Address(ipAddress, port)
    
    def createBindAddress(self, port, type = None):
        return BindIPv4Address(port)
    
    def createBroadcastAddress(self, port, type = None):
        return BroadcastIPv4Address(port)
    
    createInetAddress = classmethod(createInetAddress)
    createBindAddress = classmethod(createBindAddress)
    createBroadcastAddress = classmethod(createBroadcastAddress)
    