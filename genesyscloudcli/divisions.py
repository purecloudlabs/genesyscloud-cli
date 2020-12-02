from . import api_client
import click
import json
import sys
from . import input_util as util
from . import printer
from click.decorators import option

division_route = "/api/v2/authorization/divisions"

@click.group()
def divisions():
    """Functions to handle Divisions"""
    pass

@divisions.command()
@click.option('--full', is_flag=True, default=False)
def list(full):
    """List Divisions"""
    client = api_client.ApiClient()
    response = client.get_paged_entities(division_route)
    
    if full:
        printer.print_data(response)
    else:
        printer.print_name_id_data(response)

@divisions.command()
@click.argument("division_id")
def get(division_id):
    """List a specific division"""
    client = api_client.ApiClient()
    response = client.get(division_route+"/{}".format(division_id))
    printer.print_data(response)


@divisions.command()
@click.argument('input', nargs=-1)
def new(input):
    """Create a new Division"""
    # TODO for some reason the input is getting converted into an object and if escaped characters are supplied from the command line
    # They are not escaped correctly
    # At this point we can't handle escaped characters.

    # try for stdin
    if not sys.stdin.isatty():
        input = json.load(sys.stdin)

    data = util.get_json(input)
    client = api_client.ApiClient()
    response = client.post(division_route, data)
    printer.print_data(response)


@divisions.command()
@click.argument('division_id', nargs=1)
@click.argument('input', nargs=-1)
def update(division_id, input):
    """Update a specific Division"""

    # try for stdin
    if not sys.stdin.isatty():
        input = json.load(sys.stdin)

    data = util.get_json(input)
    client = api_client.ApiClient()
    response = client.put(division_route+"/{}".format(division_id), data)
    printer.print_data(response)


def register(cli):
    cli.add_command(divisions)