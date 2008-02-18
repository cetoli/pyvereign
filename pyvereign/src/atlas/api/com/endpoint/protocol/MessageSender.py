from atlas.api.com.endpoint.address.EndpointAddress import EndpointAddress
from atlas.api.com.endpoint.format.MessageFormat import MessageFormat
from atlas.api.env.transport.address.BroadcastIPv4Address import BroadcastIPv4Address
from atlas.util.InetAddressFactory import InetAddressFactory

class MessageSender(object):
    
    def __init__(self, endpointAddress, format):
        if not endpointAddress:
            raise RuntimeError("endpointAddress parameter is none.")
        if not isinstance(endpointAddress, EndpointAddress):
            raise TypeError("endpointAddress parameter is not an instance of EndpointAddress class.")
        self._endpointAddress = endpointAddress
        
        if not format:
            raise RuntimeError("format parameter is none.")
        if not isinstance(format, MessageFormat):
            raise TypeError("format parameter is not an instance of MessageFormat class.")
        self._format = format
    
    def sendMessage(self, message, timeout = 0):
        from atlas.api.microkernel.Microkernel import Microkernel
        
        destination = message.getDestination()
        address = None
        if destination.getInetAddress().isBroadcastAddress():
            address = InetAddressFactory.createBroadcastAddress(destination.getPort())
        else:
            address = InetAddressFactory.createInetAddress(destination.getIPAddress(), destination.getPort())
        try:
            Microkernel().executeMecanism("Environment", "transport", "sendStream", destination.getProtocol(), address, self._format.marshal(message), address.isBroadcastAddress(), timeout)
            return message
        except:
            raise
    
