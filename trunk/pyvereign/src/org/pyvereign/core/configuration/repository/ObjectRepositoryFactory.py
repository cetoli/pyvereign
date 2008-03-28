from org.pyvereign.core.configuration.configurator.AbstractConfigurator import AbstractConfigurator
from org.pyvereign.util.Constants import Constants
from org.pyvereign.util.ClassLoader import ClassLoader

class ObjectRepositoryFactory(object):
    """
    Defines a factories for creating implementations of ObjectRepository.
    @author: Fabricio
    @since: 16/01/2008 - 18:00:47
    @version: 0.0.1
    """
    
    def __new__(cls):
        """
        This method creates the unique instance of ObjectRepositoryFactory.
        @return: Returns the unique instance of ObjectRepositoryFactory.
        @rtype: L{ObjectRepositoryFactory}
        """
        if not 'instance' in cls.__dict__:
            cls.instance = object.__new__(cls)
            cls.instance.initialize()
        return cls.instance
    
    def initialize(self):
        """
        Initializes the ObjectRepositoryFactory object.
        @rtype: None
        """
        self._repositoryClasses = {}
        configurator = ObjectRepositoryFactory.ObjectRepositoryFactoryConfigurator()
        configurator.loadConfiguration()
        configurator.createObjects()
        configurator.configureObject(self)
        
    def _registerClass(self, name, classObject):
        """
        Inserts a class object in ObjectRepositoryFactory object.
        @param name: the name of mapping
        @param name: str
        @param classObject: a class object
        @type classObject: Class
        """
        if not isinstance(name, str):
            raise TypeError("name parameter is not an instance of str class.")
        self._repositoryClasses[name] = classObject
    
    def _unregisterClass(self, name):
        """
        Removes a class object in ObjectRepositoryFactory object.
        @param name: the name of mapping
        @param name: str
        """
        del self._repositoryClasses[name]
        
    def createObjectRepository(self, type):
        """
        Creates instances of ObjectRepository.
        @param type: the type of ObjectRepository
        @type type: str
        @return: Returns an instance of ObjectRepository.
        @rtype: L{ObjectRepository}
        """
        return self._repositoryClasses[type]()
        
    class ObjectRepositoryFactoryConfigurator(AbstractConfigurator):
        """
        Defines the specific configurator for ObjectRepositoryFactory.
        """
        
        def __init__(self):
            self.initialize()
            self._filename = Constants.OBJECT_REPOSITORY_FACTORY_CONFIG_FILE
            self._repository = Constants.DEFAULT_OBJECT_REPOSITORY_CLASS()
            
        def createObjects(self):
            repositories = self._configuration.getProperty("repositories")
            properties = repositories.getProperties()
            for p in properties:
                module = p.getProperty("module") 
                className = p.getProperty("classname")
                clazz = ClassLoader.loadClass(module.getValue(), className.getValue())
                self._repository.addObject(p.getName(), clazz)
                
                
        def configureObject(self, obj, configurationType = None):
            for k, v in self._repository.getObjects():
                obj._registerClass(k, v)
            return obj