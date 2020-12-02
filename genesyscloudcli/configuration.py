import configparser
import os

class Configuration:
    output_type= 'json'

    def __init__ (self):
        config_file_name = 'config'
        home = os.path.expanduser('~')
        config_file_path = os.path.join(home, '.genesyscloud', config_file_name)

        config = configparser.ConfigParser()
        
        if not os.path.isfile(config_file_path):
            return 

        config.read(config_file_path)

        self.output_type = self.get_property(config._defaults, 'output_type', 'json')

    def get_property(self, defaults,prop, default):
        if prop in defaults:
            return defaults[prop]
        
        return default
