from . import api_client
import click
import json
import sys
from . import input_util as util
from . import printer
from click.decorators import option

locations_route = "/api/v2/locations"

@click.group()
def locations():
    """Functions to handle locations"""
    pass

@locations.command()
@click.option('--full', is_flag=True, default=False)
def list(full):
    """Listing locations"""
    client = api_client.ApiClient()
    response = client.get_paged_entities(locations_route)
    
    if full:
        printer.print_data(response)
    else:
        printer.print_name_id_data(response)

@locations.command()
@click.argument("location_id")
def get(location_id):
    """List specific locations"""
    client = api_client.ApiClient()
    response = client.get(locations_route+"/{}".format(location_id))
    printer.print_data(response)


@locations.command()
@click.argument('input', nargs=-1)
def new(input):
    """Create a new Location"""
    # TODO for some reason the input is getting converted into an object and if escaped characters are supplied from the command line
    # They are not escaped correctly
    # At this point we can't handle escaped characters.

    # try for stdin
    if not sys.stdin.isatty():
        input = json.load(sys.stdin)

    data = util.get_json(input)
    client = api_client.ApiClient()
    response = client.post(locations_route, data)
    printer.print_data(response)


@locations.command()
@click.argument('location_id', nargs=1)
@click.argument('input', nargs=-1)
def update(location_id, input):
    """Update a specific Location"""

    # try for stdin
    if not sys.stdin.isatty():
        input = json.load(sys.stdin)

    data = util.get_json(input)
    client = api_client.ApiClient()
    response = client.patch(locations_route+"/{}".format(location_id), data)
    printer.print_data(response)


def register(cli):
    cli.add_command(locations)