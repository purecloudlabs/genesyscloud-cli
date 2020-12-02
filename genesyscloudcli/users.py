from yaml import error
from . import api_client
import click
import json
import sys
from . import input_util as util
from . import printer
from click.decorators import option

users_route = "/api/v2/users"

@click.group()
def users():
    """Functions to handle Users"""
    pass


@users.command()
@click.option('--full', is_flag=True, default=False)
def list(full):
    """List Users"""
    client = api_client.ApiClient()
    response = client.get_paged_entities(users_route)
    
    if full:
        printer.print_data(response)
    else:
        printer.print_name_id_data(response)


@users.command()
@click.argument('user_id')
def get(user_id):
    """Get a specific User"""
    client = api_client.ApiClient()
    response = client.get(users_route+"/{}".format(user_id))
    printer.print_data(response)


@users.command()
@click.argument('input', nargs=-1)
def new(input):
    """Create a new User"""
    # TODO for some reason the input is getting converted into an object and if escaped characters are supplied from the command line
    # They are not escaped correctly
    # At this point we can't handle escaped characters.

    # try for stdin
    if not sys.stdin.isatty():
        input = json.load(sys.stdin)

    data = util.get_json(input)
    client = api_client.ApiClient()
    response = client.post(users_route, data)
    printer.print_data(response)


@users.command()
@click.argument('user_id', nargs=1)
@click.argument('input', nargs=-1)
def update(user_id, input):
    """Update a specific User"""

    # try for stdin
    if not sys.stdin.isatty():
        input = json.load(sys.stdin)

    data = util.get_json(input)
    client = api_client.ApiClient()
    response = client.patch(users_route+"/{}".format(user_id), data)
    printer.print_data(response)
        

def register(cli):
    cli.add_command(users)