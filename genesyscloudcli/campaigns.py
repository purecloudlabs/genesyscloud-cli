from . import api_client
import click
import json
import sys
from . import input_util as util
from . import printer
from click.decorators import option

campaigns_route = "/api/v2/outbound/campaigns"

@click.group()
def campaigns():
    """Functions to handle Campaigns"""
    pass

@campaigns.command()
@click.option('--full', is_flag=True, default=False)
def list(full):
    """List Campaigns"""
    client = api_client.ApiClient()
    response = client.get_paged_entities(campaigns_route)
    
    if full:
        printer.print_data(response)
    else:
        printer.print_name_id_data(response)

@campaigns.command()
@click.argument("campaign_id")
def get(campaign_id):
    """List a specific Campaign"""
    print(campaign_id)
    client = api_client.ApiClient()
    response = client.get(campaigns_route+"/{}".format(campaign_id))
    printer.print_data(response)


@campaigns.command()
@click.argument('input', nargs=-1)
def new(input):
    """Create a new Campaign"""
    # TODO for some reason the input is getting converted into an object and if escaped characters are supplied from the command line
    # They are not escaped correctly
    # At this point we can't handle escaped characters.

    # try for stdin
    if not sys.stdin.isatty():
        input = json.load(sys.stdin)

    data = util.get_json(input)
    client = api_client.ApiClient()
    response = client.post(campaigns_route, data)
    printer.print_data(response)


@campaigns.command()
@click.argument('campaign_id', nargs=1)
@click.argument('input', nargs=-1)
def update(campaign_id, input):
    """Update a specific Campaign"""

    # try for stdin
    if not sys.stdin.isatty():
        input = json.load(sys.stdin)

    data = util.get_json(input)
    client = api_client.ApiClient()
    response = client.put(campaigns_route+"/{}".format(campaign_id), data)
    printer.print_data(response)


def register(cli):
    cli.add_command(campaigns)