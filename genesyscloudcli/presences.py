from . import api_client
import click
import json
import sys
from . import input_util as util
from . import printer
from click.decorators import option

presence_route = "/api/v2/presencedefinitions"

@click.group()
def presence():
    """Functions to handle Divisions"""
    pass

@presence.command()
@click.option('--full', is_flag=True, default=False)
def list(full):
    """Listing Presence Definitions"""
    client = api_client.ApiClient()
    response = client.get_paged_entities(presence_route)
    
    if full:
        printer.print_data(response)
    else:
        printer.print_name_id_data(response)
    

@presence.command()
@click.argument("presence_id")
def get(presence_id):
    """List specific Presence Definition"""
    client = api_client.ApiClient()
    response = client.get(presence_route+"/{}".format(presence_id))
    printer.print_data(response)


@presence.command()
@click.argument('input', nargs=-1)
def new(input):
    """Create a new Presence"""
    # TODO for some reason the input is getting converted into an object and if escaped characters are supplied from the command line
    # They are not escaped correctly
    # At this point we can't handle escaped characters.

    # try for stdin
    if not sys.stdin.isatty():
        input = json.load(sys.stdin)

    data = util.get_json(input)
    client = api_client.ApiClient()
    response = client.post(presence_route, data)
    printer.print_data(response)


@presence.command()
@click.argument('presence_id', nargs=1)
@click.argument('input', nargs=-1)
def update(presence_id, input):
    """Update a specific Presence"""

    # try for stdin
    if not sys.stdin.isatty():
        input = json.load(sys.stdin)

    data = util.get_json(input)
    client = api_client.ApiClient()
    response = client.put(presence_route+"/{}".format(presence_id), data)
    printer.print_data(response)


def register(cli):
    cli.add_command(presence)