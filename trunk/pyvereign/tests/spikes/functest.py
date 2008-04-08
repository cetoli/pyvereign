from org.pyvereign.core.environment.DefaultTransportService import DefaultTransportService
from org.pyvereign.core.environment.Environment import Environment
from org.pyvereign.core.microkernel.CoreServiceRequest import CoreServiceRequest
from org.pyvereign.core.id.IDFactory import IDFactory

service = DefaultTransportService()
environment = Environment()
environment.addModule(IDFactory().createCoreServiceID(environment, service), service)
request = CoreServiceRequest(IDFactory().createCoreServiceID(environment, service), "getStatus")
print environment.executeService(request)