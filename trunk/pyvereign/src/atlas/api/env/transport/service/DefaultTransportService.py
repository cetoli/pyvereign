from atlas.api.env.transport.service.AbstractTransportService import AbstractTransportService
from atlas.api.env.transport.forwarder.ForwarderFactory import ForwarderFactory
from atlas.api.env.transport.address.InetAddress import InetAddress
from atlas.api.exception.TransportError import TransportError
from atlas.api.env.transport.receiver.ReceiverFactory import ReceiverFactory
from atlas.api.env.transport.address.BindIPv4Address import BindIPv4Address
from atlas.api.env.transport.listener.StreamListener import StreamListener

class DefaultTransportService(AbstractTransportService):
    
    def __init__(self):
        self._name = "transport"
        
    def initialize(self, environment):
        AbstractTransportService.initialize(self, environment)
        
    def start(self, *params):
        protocols = self._environment.executeService("protocol", "getProtocols")
        
        self._protocols = {}
        self._streamListeners = {}
        for p in protocols:
            self._protocols[p.getName()] = p
            receiver = ReceiverFactory().createForwarder(p.getName(), BindIPv4Address(5051), p)
            listener = StreamListener(self._environment, receiver)
            print "Starting listener in "+p.getName()+"://"+receiver.getInetAddress().getIPAddress()+":"+str(receiver.getInetAddress().getPort())
            listener.open()
            receiver.reuseAddress(True)
            listener.start()
            self._streamListeners[p.getName()] = listener
            print "Listener in "+p.getName()+"://"+receiver.getInetAddress().getIPAddress()+":"+str(receiver.getInetAddress().getPort())+" was started."
        
    def sendStream(self, protocolName, inetAddress, stream, broadcasting = False, timeout = 0):
        if not protocolName:
            raise RuntimeError("protocolName parameter is none.")
        if not isinstance(protocolName, str):
            raise TypeError("protocolName parameter is not an instance of str class.")
        if not inetAddress:
            raise RuntimeError("inetAddress parameter is none.")
        if not isinstance(inetAddress, InetAddress):
            raise TypeError("inetAddress parameter is not an instance of InetAddress class.")
        if not stream:
            raise RuntimeError("stream parameter is none.")
        if not isinstance(protocolName, str):
            raise TypeError("stream parameter is not an instance of str class.")
        if broadcasting == None:
            raise RuntimeError("broadcasting parameter is none.")
        if not isinstance(protocolName, str):
            raise TypeError("broadcasting parameter is not an instance of bool class.")
        
        forwarder = ForwarderFactory().createForwarder(protocolName, inetAddress, self._protocols[protocolName])
        try:
            try:
                forwarder.open()
                if inetAddress.isBroadcastAddress() and broadcasting == True:
                    forwarder.supportBroadcasting(broadcasting)
                if not inetAddress.isBroadcastAddress() and broadcasting == True:
                    raise TransportError("Invalid configuration for the broadcasting of stream.")
                if timeout > 0:
                    forwarder.setTimeout(timeout)
                elif timeout < 0:
                    raise TransportError("Invalid timeout value.")
                return forwarder.send(stream)
            except:
                raise
        finally:
            forwarder.close()
            
    

    def stop(self):
        for l in self._streamListeners.values():
            l.close()
        return True