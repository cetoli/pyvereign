from atlas.api.env.transport.receiver.Receiver import Receiver

class AbstractReceiver(Receiver):
    
    def initialize(self):
        self._inetAddress = None
        self._socket = None
        self._opened = False
        self._protocol = None
    
    def close(self):
        try:
            if not self._socket:
                self._socket.close()
            return True
        except:
            raise