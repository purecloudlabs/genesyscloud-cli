from . import analytics
from . import campaigns
from . import chat
import click
from . import contact_lists
from . import divisions
from . import groups
from . import http
from . import locations
from . import notifications
from . import organization
from . import presences
from . import profile_command
from . import queues
from . import search
from . import skills
from . import users

@click.group()
@click.option('--output', default="", help='Output format for commands (json, yaml, table)')
@click.option('--profile', default="", help='Which configured profile to use')
@click.option('--page-size', default=250, help='Set a page size other')
@click.option('--page', default=-1, help='Return a specific page')
@click.option('--debug', default=-1, help='Return a specific page')
def cli(output, profile, page_size, page, debug):
    """The Genesys Cloud cli is a tool to interact with Genesys Cloud"""
    click.get_current_context().meta['output'] = output
    click.get_current_context().meta['profile'] = profile
    click.get_current_context().meta['page_size'] = page_size
    click.get_current_context().meta['page'] = page    
    click.get_current_context().meta['debug'] = debug    
    

analytics.register(cli)
campaigns.register(cli)
profile_command.register(cli)
chat.register(cli)
notifications.register(cli)
contact_lists.register(cli)
divisions.register(cli)
groups.register(cli)
http.register(cli)
locations.register(cli)
organization.register(cli)
presences.register(cli)
queues.register(cli)
skills.register(cli)
search.register(cli)
users.register(cli)
