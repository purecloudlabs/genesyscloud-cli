from . import api_client
import click
from . import printer
from click.decorators import option

from . import input_util as util
import sys

@click.command()
@click.argument('uri')
def get(uri):
    """Performs a HTTP GET on the specified URI.  Uri should be just the path eg /api/v2/users"""
    client = api_client.ApiClient()
    response = client.get(uri)
    printer.print_data(response)
  
@click.command()
@click.argument('uri')
@click.argument('body')
def post(uri, body):
    # try for stdin
    if not sys.stdin.isatty():
        input = json.load(sys.stdin)

    data = util.get_json(body)
    
    """Performs a HTTP POST on the specified URI"""
    client = api_client.ApiClient()
    response = client.post(uri, data)
    printer.print_data(response)

def register(cli):
    cli.add_command(get)    
    cli.add_command(post)    