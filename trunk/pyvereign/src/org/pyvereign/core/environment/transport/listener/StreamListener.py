from threading import Thread
from org.pyvereign.core.environment.transport.listener.TransportListener import TransportListener

class StreamListener(Thread):
    """
    Implements a passive thread for receiving streams which were sended by other user computers.
    
    @author: Fabricio
    @since: 
    @version: 
    """
    
    def __init__(self, receiver):
        """
        Initializes the StreamListener object.
        
        @param receiver: a Receiver object.
        @type receiver: L{Receiver}
        """
        Thread.__init__(self)
        self._receiver = receiver
        """
        @ivar: the receiver of listener.
        @type: L{Receiver}  
        """
        self._bufferSize = 1024
        """
        @ivar: the buffer size for stream receiving.
        @type: int  
        """
        self._active = False
        """
        @ivar: flag to determinate if the thread object is active.
        @type: bool  
        """
        self._transportListeners = {}
        """
        @ivar: the map of transport listeners.
        @type: dict  
        """
        self._id = ""
    
    def addTransportListener(self, uri, listener):
        """
        Adds a mapping of a uri with a transport listener.
        
        @param uri: an uri
        @type uri: str
        @param listener: a TransportListener object
        @type listener: L{TransportListener} 
        @return: Returns the mapped listener.
        @rtype: L{TransportListener}
        """
        if not uri:
            raise RuntimeError("uri is none.")
        if not isinstance(uri, str):
            raise TypeError("uri is not an instance of str class.")
        if not listener:
            raise RuntimeError("listener is none.")
        if not isinstance(listener, TransportListener):
            raise TypeError("listener is not an instance of TransportListener class.")
        self._transportListeners[uri] = listener
        print uri
        return self._transportListeners[uri]
    
    def removeTransportListener(self, uri):
        """
        Removes the TransportListener object mapped in the uri.
        
        @param uri: an uri
        @type uri: str
        @return: Returns the removed listener.
        @rtype: L{TransportListener}
        """
        if not uri:
            raise RuntimeError("uri is none.")
        if not isinstance(uri, str):
            raise TypeError("uri is not an instance of str class.")
        listener = self._transportListeners[uri]
        del self._transportListeners[uri]
        return listener
    
    def getTransportListener(self, uri):
        """
        Gets the TransportListener object mapped in the uri.
        
        @param uri: an uri
        @type uri: str
        @return: Returns the mapped listener.
        @rtype: L{TransportListener}
        """
        if not uri:
            raise RuntimeError("uri is none.")
        if not isinstance(uri, str):
            raise TypeError("uri is not an instance of str class.")
        return self._transportListeners[uri]
    
    def getNumberOfTransportListeners(self):
        """
        Gets the total of TransportListener objects in map.
        
        @return: Returns the total of TransportListener objects in map.
        @rtype: int
        """
        return len(self._transportListeners)
    
    def setBufferSize(self, bufferSize):
        """
        Sets the buffer size for receiving of streams.
        
        @param bufferSize: the buffer size for receiving of streams.
        @type bufferSize: int
        @return: Returns the buffer size for receiving of streams.
        @rtype: int
        """
        if not bufferSize:
            raise RuntimeError("bufferSize is none.")
        if bufferSize <= 0:
            raise RuntimeError("negative or zero bufferSize")
        if not isinstance(bufferSize, int):
            raise TypeError("bufferSize is not an instance of int class.")
        self._bufferSize = bufferSize
        return self._bufferSize
        
    def getBufferSize(self):
        """
        Gets the buffer size for receiving of streams.
        
        @return: Returns the buffer size for receiving of streams.
        @rtype: int
        """
        return self._bufferSize
    
    def isActive(self):
        """
        Vreifies if listener is active.
        
        @return: Returns if listener is active.
        @rtype: bool
        """
        return self._active
    
    def reuseAddress(self, flag):
        """
        Configure the receiver of StreamListener to reuse the local address whether true.
        
        @return: Returns true if the receiver of StreamListener was configured.
        @rtype: bool
        """
        if flag == None:
            raise RuntimeError("flag is none.")
        if not isinstance(flag, bool):
            raise TypeError("flag is not an instance of bool class.")
        return self._receiver.reuseAddress(flag)
    
    def open(self, port):
        """
        Binds the StreamListener object to a communication port.
        
        @param port: the communication port
        @type port: int
        """
        if not port:
            raise RuntimeError("port is none.")
        if port <= 0:
            raise RuntimeError("negative or zero port.")
        if not isinstance(port, int):
            raise TypeError("port is not an instance of int class.")
        try:
            self._receiver.getInetAddress().setPort(port)
            return self._receiver.open()
        except:
            raise
    
    def run(self):
        """
        Runs the StreamListener object.
        @rtype: None
        """
        try:
            try:
                self._active = self._receiver.bind()
                while self._active:
                    stream = self._receiver.receive(self._bufferSize)
                    if stream:
                        if self._id == stream:
                            break
                        for listener in self._transportListeners.values():
                            listener.processStream(stream)
                print "passou"        
            except:
                raise
        finally:
            self._receiver.close()
    
    
    def close(self):
        """
        Closes the StreamListener object.
        
        @return: 
        @rtype: bool
        """
        return True
    
    