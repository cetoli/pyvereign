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
    HARDWARES_CONFIG_FILE = "hardwares.json"
    
    SYSTEM_ELEMENTS_CONFIG_FILE = "system_elements.json"
    
    NETWORKING_ELEMENTS_CONFIG_FILE = "networking_elements.json"
    
    ENVIRONMENT_CONFIG_FILE = "environment.json"
    
    MESSAGE_FORMATS_CONFIG_FILE = "formats.json"
    
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
    
    ######################################################################################
    #                        Constants of Hardware                                       #
    ######################################################################################
    
    MACHINE = "MACHINE"
    PROCESSOR = "PROCESSOR"
    DISK_DRIVE = "DISK_DRIVE"
    PHYSICAL_MEMORY = "PHYSICAL_MEMORY" 
    BATTERY = "BATTERY"
    NETWORK_ADAPTER = "NETWORK_ADAPTER"
    
    ######################################################################################
    #                        Constants of System Elements                                #
    ######################################################################################
    
    PROCESS = "PROCESS"
    
    ######################################################################################
    #                        Constants of Networking Elements                            #
    ######################################################################################
    
    NETWORK_PROTOCOL = "NETWORK_PROTOCOL"
    
    ######################################################################################
    #                              Names of Internal Servers                             #
    ######################################################################################
    
    ENVIRONMENT = "environment"
    
    ######################################################################################
    #                              Names of Core Services                                #
    ######################################################################################
    
    TRANSPORT_SERVICE = "transport"
    NETWORKING_SERVICE = "networking"
    
    ######################################################################################
    #                              Names of Message Formats                              #
    ######################################################################################
    
    JSON = "JSON"