from org.pyvereign.core.configuration.repository.DefaultObjectRepository import DefaultObjectRepository
class Constants:
    """
    Defines all constants of platform.
    
    @author: Fabricio
    @since: 18/03/2008 - 17:22:20
    @version: 0.0.1
    """
    
    ######################################################################################
    #                            Names of configuration files                            #
    ######################################################################################
    
    MICROKERNEL_CONFIG_FILE = "microkernel.json"
    """
    @cvar: configuration file of microkernel
    @type: L{str}  
    """
    OBJECT_REPOSITORY_FACTORY_CONFIG_FILE = "object_repository_factory.json"
    """
    @cvar: configuration file of object repository factory.
    @type: L{str}  
    """
    
    ######################################################################################
    #                            Default Class Objects                                   #
    ######################################################################################
    
    DEFAULT_OBJECT_REPOSITORY_CLASS = DefaultObjectRepository
    """
    @cvar: Default object repository class.
    @type: L{DefaultObjectRepository}  
    """
    
    ######################################################################################
    #                        Constants of Object Repository Factory                      #
    ######################################################################################
    
    DEFAULT_OBJECT_REPOSITORY = "DEFAULT_OBJECT_REPOSITORY"
    """
    @cvar: Constant for mapping DefaultObjectRepository class.
    @type: L{str}  
    """
    