import configparser
import os
import click
import sys
class Profile:
    environment='mypurecloud.com'
    client_id=''
    client_secret=''
    name = ''

    def __str__(self):
        return "name:{}\nenvironment:{}\nclient_id:{}".format(self.name, self.environment, self.client_id)


class ProfileHandler:
    def get_profile(self):

        name = click.get_current_context().meta['profile'].lower()

        credentials = self.get_credentials_file()

        profile = Profile()

        if name == 'default' or len(name) == 0:

            profile.environment = credentials._defaults['environment']
            profile.client_id = credentials._defaults['client_id']
            profile.client_secret = credentials._defaults['client_secret']
            if 'name' in credentials._defaults:
                profile.name = credentials._defaults['name']
            return profile

        if not credentials.has_section(name):
            print("profile {} not found".format(name))
            sys.exit(1)
            return

        profile.environment = credentials[name]['environment']
        profile.client_id = credentials[name]['client_id']
        profile.client_secret = credentials[name]['client_secret']
        if 'name' in credentials[name]:
            profile.name = credentials[name]['name']

        return profile
    
    def new_profile(self):
        config = self.get_credentials_file()

        profile = input('Profile Name [DEFAULT]: ')
        environment = input('Genesys Cloud Environment (mypurecloud.com, usw2.pure.cloud): ')
        client_id = input('OAuth Client ID: ')
        client_secret = input('OAuth Client Secret: ')

        if len(profile) == 0:
            properties = {
                'client_id' : client_id,
                'client_secret' : client_secret,
                'environment' : environment
            }
            config._defaults = properties
        else:
            profile = profile.lower()

            if not config.has_section(profile):
                config.add_section(profile)
            
            config.set(profile, "client_id", client_id)
            config.set(profile, "client_secret", client_secret)
            config.set(profile, "environment", environment)

        self.save_credentials_file(config)


    def set_default(self, name):
        config = self.get_credentials_file()
        name = name.lower()
        properties = {
                'client_id' : config.get(name, 'client_id'),
                'client_secret' : config.get(name, 'client_secret'),
                'environment' : config.get(name, 'environment'),
                'profile' : name
            }
        config._defaults = properties
        self.save_credentials_file(config)


    def get_credentials_file(self):
        config_file_name = 'credentials'
        home = os.path.expanduser('~')
        config_file_path = os.path.join(home, '.genesyscloud', config_file_name)

        config = configparser.ConfigParser()
        
        # Get the current users home directory and check the ~/.genesyscloud/credential file exists
        if not os.path.isfile(config_file_path):
            return config

        config.read(config_file_path)
        return config


    def save_credentials_file(self, config):
        config_file_name = 'credentials'
        home = os.path.expanduser('~')
        config_file_path = os.path.join(home, '.genesyscloud', config_file_name)

        with open(config_file_path, 'w') as configfile:
            config.write(configfile)


    def get_sections(self):
        config = self.get_credentials_file()
        return config.sections()