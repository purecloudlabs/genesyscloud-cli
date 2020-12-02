from . import api_client
import click
import json
import sys
from . import input_util as util
from . import printer
from click.decorators import option

contactlists_route = "/api/v2/outbound/contactlists"

@click.group()
def contactlists():
    """Functions to handle Contact Lists"""
    pass

@contactlists.command()
@click.option('--full', is_flag=True, default=False)
def list(full):
    """Listing Contact Lists"""
    client = api_client.ApiClient()
    response = client.get_paged_entities(contactlists_route)
    
    if full:
        printer.print_data(response)
    else:
        printer.print_name_id_data(response)

@contactlists.command()
@click.argument("contactlist_id")
def get(contactlist_id):
    """List specific Contact List"""
    client = api_client.ApiClient()
    response = client.get(contactlists_route+"/{}".format(contactlist_id))
    printer.print_data(response)


@contactlists.command()
@click.argument('input', nargs=-1)
def new(input):
    """Create a new ContactList"""
    # TODO for some reason the input is getting converted into an object and if escaped characters are supplied from the command line
    # They are not escaped correctly
    # At this point we can't handle escaped characters.

    # try for stdin
    if not sys.stdin.isatty():
        input = json.load(sys.stdin)

    data = util.get_json(input)
    client = api_client.ApiClient()
    response = client.post(contactlists_route, data)
    printer.print_data(response)


@contactlists.command()
@click.argument('contactlist_id', nargs=1)
@click.argument('input', nargs=-1)
def update(contactlist_id, input):
    """Update a specific ContactList"""

    # try for stdin
    if not sys.stdin.isatty():
        input = json.load(sys.stdin)

    data = util.get_json(input)
    client = api_client.ApiClient()
    response = client.put(contactlists_route+"/{}".format(contactlist_id), data)
    printer.print_data(response)


def register(cli):
    cli.add_command(contactlists)