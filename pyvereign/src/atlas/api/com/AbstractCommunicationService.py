from atlas.api.com.CommunicationService import CommunicationService
from atlas.api.com.Communication import Communication

class AbstractCommunicationService(CommunicationService):
    
    def initialize(self, communication):
        if not communication:
            raise RuntimeError("communication parameter is none.")
        if not isinstance(communication, Communication):
            raise TypeError("communication parameter is not an instance of Communication class.")
        self._communication = communication
        self._name = ""
    
    def getName(self):
        return self._name