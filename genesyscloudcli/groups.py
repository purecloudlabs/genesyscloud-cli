from . import api_client
import click
import json
import sys
from . import input_util as util
from . import printer
from click.decorators import option

group_route = "/api/v2/groups"

@click.group()
def groups():
    """Functions to handle Groups"""
    pass

@groups.command()
@click.option('--full', is_flag=True, default=False)
def list(full):
    """Listing Groups"""
    client = api_client.ApiClient()
    response = client.get_paged_entities(group_route)
    
    if full:
        printer.print_data(response)
    else:
        printer.print_name_id_data(response)

@groups.command()
@click.argument('group_id')
def get(group_id):
    """List a specific Group"""
    client = api_client.ApiClient()
    response = client.get(group_route+"/{}".format(group_id))
    printer.print_data(response)


@groups.command()
@click.argument('input', nargs=-1)
def new(input):
    """Create a new Group"""
    # TODO for some reason the input is getting converted into an object and if escaped characters are supplied from the command line
    # They are not escaped correctly
    # At this point we can't handle escaped characters.

    # try for stdin
    if not sys.stdin.isatty():
        input = json.load(sys.stdin)

    data = util.get_json(input)
    client = api_client.ApiClient()
    response = client.post(group_route, data)
    printer.print_data(response)


@groups.command()
@click.argument('group_id', nargs=1)
@click.argument('input', nargs=-1)
def update(group_id, input):
    """Update a specific Group"""

    # try for stdin
    if not sys.stdin.isatty():
        input = json.load(sys.stdin)

    data = util.get_json(input)
    client = api_client.ApiClient()
    response = client.put(group_route+"/{}".format(group_id), data)
    printer.print_data(response)


def register(cli):
    cli.add_command(groups)