from atlas.api.com.CommunicationService import CommunicationService


class AbstractCommunicationService(CommunicationService):
    
    def initialize(self, communication):
        if not communication:
            raise RuntimeError("communication parameter is none.")
        from atlas.api.com.Communication import Communication
        if not isinstance(communication, Communication):
            raise TypeError("communication parameter is not an instance of Communication class.")
        self._communication = communication
        self._name = ""
        self._status = CommunicationService.INITIALIZED
    
    def start(self, *params):
        self._status = CommunicationService.STARTED

    def stop(self):
        self._status = CommunicationService.STOPED
    
    def getName(self):
        return self._name
    
    def getStatus(self):
        return self._status